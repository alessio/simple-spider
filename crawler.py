import argparse
import os
import sys
import scrapy

PROGNAME = os.path.basename(sys.argv[0])


class WebSpider(scrapy.Spider):
    pass


def crawl(settings, start_urls, allowed_domains, output_document):
    pass

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
