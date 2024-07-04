"""How to build an AI that can answer questions about your website.

Reference:
    https://platform.openai.com/docs/tutorials/web-qa-embeddings
"""

import argparse
import logging
import os
import re
import urllib.request
from collections import deque
from html.parser import HTMLParser
from typing import Optional
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


class HyperlinkParser(HTMLParser):
    """Parse the hyperlinks and store it in self.hyperlinks."""

    def __init__(self) -> None:
        super().__init__()
        self.hyperlinks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])


def get_hyperlinks(url: str) -> list[str]:
    try:
        with urllib.request.urlopen(url) as response:
            if not response.info().get("Content-Type").startswith("text/html"):
                return []
            html = response.read().decode("utf-8")
    except Exception as e:
        logging.warn(e)
        return []

    parser = HyperlinkParser()
    parser.feed(html)

    return list(set(parser.hyperlinks))


def get_domain_hyperlinks(
    local_domain: str, url: str, http_url_pattern: str = r"^http[s]*://.+"
) -> list[str]:
    clean_links = []
    for link in set(get_hyperlinks(url)):
        clean_link: Optional[str] = None

        # If the link is a URL, check if it is within the same domain
        if re.search(http_url_pattern, link):
            # Parse the URL and check if the domain is the same
            if urlparse(link).netloc == local_domain:
                clean_link = link
        # If the link is not a URL, check if it is a relative link
        else:
            if link.startswith("/"):
                link = link[1:]
            elif link.startswith("#") or link.startswith("mailto:"):
                continue
            clean_link = "https://" + local_domain + "/" + link

        if clean_link:
            if clean_link.endswith("/"):
                clean_link = clean_link[:-1]
            clean_links.append(clean_link)

    # Return the list of hyperlinks that are within the same domain
    return list(set(clean_links))


def save_html_as_txt(out_dir: str, url: str) -> None:
    txt_name = os.path.join(out_dir, f"{url[8:].replace('/', '_')}.txt")
    with open(txt_name, "w", encoding="utf-8") as f:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        text = soup.get_text()
        if "You need to enable JavaScript to run this app." in text:
            logging.warning("Unable to parse page %s due to JavaScript being required", url)
        f.write(text)


def crawl(url: str, max_depth: int) -> None:
    local_domain = urlparse(url).netloc

    out_dir = os.path.join("parsed", local_domain)
    os.makedirs(out_dir, exist_ok=True)

    queue = deque([(url, 0)])
    seen = set([url])
    while queue:
        url, depth = queue.pop()
        logging.info("process %s", url)

        save_html_as_txt(out_dir, url)

        for link in get_domain_hyperlinks(local_domain, url):
            next_depth = depth + 1
            if link in seen or next_depth > max_depth:
                continue
            queue.append((link, next_depth))
            seen.add(link)


parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, required=True)
parser.add_argument("--max-depth", type=int, default=3)
args = parser.parse_args()


crawl(args.url, args.max_depth)
