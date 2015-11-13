from collections import defaultdict
from functools import partial
from unittest import TestCase
from urlparse import urlparse

from scrapy.crawler import CrawlerProcess

import crawler


class WebsiteStandardTest(TestCase):

    @classmethod
    def setUpClass(self):
        self.results = defaultdict(partial(defaultdict, set))
        self.domain = "thisisglow.com"
        self.url = "http://thisisglow.com/"

        settings = {"LOG_ENABLED": False}
        process = CrawlerProcess(settings)
        process.crawl(
            crawler.WebSpider,
            results=self.results,
            allowed_domains=[self.domain],
            start_urls=[self.url],
        )
        process.start()

    def test_start_page_crawled(self):
        self.assertIn(
            "http://thisisglow.com/",
            self.results,
        )

    def test_page_crawled(self):
        self.assertIn(
            "http://thisisglow.com/contact-us/",
            self.results["http://thisisglow.com/"]["links"],
        )
        self.assertIn(
            "http://thisisglow.com/contact-us/",
            self.results,
        )

    def test_links_within_allowed_domain(self):
        for child in self.results["http://thisisglow.com/"]["links"]:
            self.assertEqual(urlparse(child).netloc, self.domain)

    def test_external_outside_domain(self):
        for link in self.pages["http://thisisglow.com/"]["external"]:
            self.assertNotEqual(urlparse(link).netloc, self.domain)

    def test_external_not_visited(self):
        page = "http://thisisglow.com/managed-services/"
        external_page = "http://twitter.com/thisisglow"

        self.assertIn(external_page, self.pages[page]["external"])
        self.assertNotIn(external_page, self.pages)
