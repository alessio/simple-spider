from __future__ import print_function
import argparse
from collections import defaultdict
from functools import partial
from urlparse import (
    urljoin,
    urlparse,
)
import json
import os
import sys

import scrapy
from scrapy.crawler import CrawlerProcess

PROGNAME = os.path.basename(sys.argv[0])


class JSONEncoder(json.JSONEncoder):
    """
    Extend json's default encoder to support the 'set' type.

    'set' is Python-specific, thus JSON doesn't support it.
    A common practice is to convert sets into lists, which are
    natively supported by the the JSON specifications.
    """

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        else:
            return super(JSONEncoder, self).default(obj)


class WebSpider(scrapy.Spider):
    """
    Scrape a webpage looking for 'a', 'area', 'img', and 'script' tags.

    Handle the following schemes:
     - http://
     - https://
     - ftp://
    """
    name = 'webspider'
    allowed_schemes = ("http", "https", "ftp")
    xpath_pattern = (
        '//img/@src | //script/@src | //a/@href |'
        '//iframe/@src | //area/@src'
    )

    def __init__(self, allowed_domains, start_urls, results, *args, **kw):
        super(WebSpider, self).__init__(*args, **kw)
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls
        self.results = results
        self.visited = set()

    def hostname_allowed(self, hostname):
        if hostname is not None:
            return any(hostname.endswith(ad) for ad in self.allowed_domains)
        return False

    def parse(self, response, **kwargs):
        current_url = response.url
        if not hasattr(response, "xpath"):
            parent = kwargs.get("parent")
            self.results[parent]['links'].add(current_url)
            return
        for link in response.xpath(self.xpath_pattern).extract():
            link = urljoin(current_url, link)
            link_parsed = urlparse(link)
            if link_parsed.scheme in self.allowed_schemes:
                if self.hostname_allowed(link_parsed.netloc):
                    self.visited.add(link)
                    self.results[current_url]['links'].add(link)
                    yield scrapy.Request(
                        link, callback=partial(self.parse, parent=current_url),
                    )
                else:
                    self.results[current_url]['external'].add(link)


def crawl(settings, start_urls, allowed_domains, output_document):
    """
    Set up the crawlers as per client's parameters.
    Output's a JSON sitemap.
    """
    results = defaultdict(partial(defaultdict, set))
    process = CrawlerProcess(settings)
    process.crawl(
        WebSpider,
        results=results,
        allowed_domains=args.allowed_domains,
        start_urls=args.start_urls,
    )
    process.start()
    print(json.dumps(results, cls=JSONEncoder), file=output_document)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=PROGNAME,
        description="Generate a JSON sitemap for website.",
    )
    parser.add_argument(
        "-u", "--start-urls", dest="start_urls", nargs="+",
        help="URLs where the spider will start to crawl from"
    )
    parser.add_argument(
        "-d", "--allowed-domains", dest="allowed_domains", nargs="+",
        help="List of domains that the spider is allowed to crawl"
    )
    parser.add_argument(
        "-D", "--debug", dest="debug", action="store_true", default=False,
        help="Enable debug output",
    )
    parser.add_argument(
        "-O", "--output-document",
        dest="output_document",
        type=argparse.FileType("w"),
        default=sys.stdout,
        metavar="FILE",
        help="Write output to FILE instead of stdout",
    )
    args = parser.parse_args()
    sys.exit(
        crawl(
            settings={"LOG_ENABLED": args.debug},
            start_urls=args.start_urls,
            allowed_domains=args.allowed_domains,
            output_document=args.output_document,
        )
    )
