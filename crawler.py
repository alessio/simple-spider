import argparse
import os
import sys
import scrapy

PROGNAME = os.path.basename(sys.argv[0])


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

    def __init__(self, allowed_domains, start_urls, results, *args, **kw):
            super(WebSpider, self).__init__(*args, **kw)
            self.allowed_domains = allowed_domains
            self.start_urls = start_urls
            self.results = results

    def parse(self):
        # STUB
        pass


def crawl(settings, start_urls, allowed_domains, output_document):
    # STUB
    results = {}
    WebSpider(
        results=results,
        allowed_domains=args.allowed_domains,
        start_urls=args.start_urls,
    )

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
