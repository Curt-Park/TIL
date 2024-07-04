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

# Regex pattern to match a URL
HTTP_URL_PATTERN = r"^http[s]*://.+"


class HyperlinkParser(HTMLParser):

    def __init__(self) -> None:
        super().__init__()
        self.hyperlinks: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])


def get_hyperlinks(url: str) -> list[str]:
    with urllib.request.urlopen(url) as response:
        if not response.info().get("Content-Type").startswith("text/html"):
            return []
        html = response.read().decode("utf-8")
    parser = HyperlinkParser()
    parser.feed(html)
    return list(set(parser.hyperlinks))


def get_domain_hyperlinks(local_domain: str, url: str) -> list[str]:
    clean_links = []
    for link in get_hyperlinks(url):
        if link.startswith("#") or link.startswith("mailto:"):
            continue
        url_pattern_matched = re.search(HTTP_URL_PATTERN, link) is not None
        if url_pattern_matched and urlparse(link).netloc != local_domain:
            continue

        link = link.startswith("/") and link[1:] or link
        link = link.endswith("/") and link[:-1] or link

        if url_pattern_matched:
            clean_links.append(link)
        else:
            clean_links.append("https://" + local_domain + "/" + link)

        return list(set(clean_links))


def crawl(url: str) -> None:
    local_domain = urlparse(url).netloc
    queue = deque([url])
    seen = set([url])

    out_dir = os.path.join("parsed", local_domain)
    os.makedirs(out_dir, exist_ok=True)

    while queue:
        url = queue.pop()
        logging.info("process %s", url)

        with open(
            os.path.join(out_dir, f"{url[8:].replace('/', '_')}.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            text = soup.get_text()
            if "You need to enable JavaScript to run this app." in text:
                logging.warn(
                    "Unable to parse page %s due to JavaScript being required", url
                )
            f.write(text)

        for link in get_domain_hyperlinks(local_domain, url):
            if link in seen:
                continue
            queue.append(link)
            seen.add(link)


parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, required=True)
args = parser.parse_args()


crawl(args.url)
