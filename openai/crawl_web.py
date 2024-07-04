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
        """Override handle_starttag."""
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])


def get_hyperlinks(url: str) -> list[str]:
    """Get hyperlinks without duplicates."""
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
    """Get valid hyperlinks with the same local domain."""
    clean_links = []
    for link in get_hyperlinks(url):
        # Skip.
        url_pattern_matched = re.search(http_url_pattern, link) is not None
        if url_pattern_matched and urlparse(link).netloc != local_domain:
            logging.info("skip %s due to unmatched local domain", link)
            continue
        if not url_pattern_matched and link.startswith("#") or link.startswith("mailto:"):
            logging.info("skip %s due to invalid hyperlink", link)
            continue

        # Format.
        clean_link = link
        clean_link = clean_link if not link.startswith("/") else clean_link[1:]
        clean_link = clean_link if not clean_link.endswith("/") else clean_link[:-1]
        clean_link = clean_link if url_pattern_matched else f"https://{local_domain}/{clean_link}"

        # Append.
        clean_links.append(clean_link)

    # Return the list of hyperlinks that are within the same domain
    return list(set(clean_links))


def save_html_as_txt(out_dir: str, url: str) -> None:
    """Save html as {out_dir}/{u_r_l}.txt."""
    txt_name = os.path.join(out_dir, f"{url[8:].replace('/', '_')}.txt")
    with open(txt_name, "w", encoding="utf-8") as f:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        text = soup.get_text()
        if "You need to enable JavaScript to run this app." in text:
            logging.warning("Unable to parse page %s due to JavaScript being required", url)
        f.write(text)


def crawl(url: str, max_depth: int) -> None:
    """Crawl web-pages that doesn't exceed the max_depth."""
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--max-depth", type=int, default=3)
    args = parser.parse_args()
    crawl(args.url, args.max_depth)


main()
