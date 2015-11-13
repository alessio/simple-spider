# Summary

This is simple web crawler that, given a list of starting URLs, visits all pages within the given domains.
The output is a plain JSON file whose structure meets the following specification:
```
{
    "http://www.example.com/starting_page_1.html": {
        "links": [
            "http://www.example.com/static/js/main.js",
            "http://www.example.com/static/images/picture.png"
            "http://www.example.com/blog/post/"
        ],
        "external": [
            "http://twitter.com/aTwitterAccount",
            
        ]
    }
}
```

# Installation

Just run:
```
pip install -r requirements.txt
```

# Usage
```shell
$ python crawler.py -h
usage: crawler.py [-h] [-u START_URLS [START_URLS ...]]
                  [-d ALLOWED_DOMAINS [ALLOWED_DOMAINS ...]] [-D] [-O FILE]

Generate a JSON sitemap for website.

optional arguments:
  -h, --help            show this help message and exit
  -u START_URLS [START_URLS ...], --start-urls START_URLS [START_URLS ...]
                        URLs where the spider will start to crawl from
  -d ALLOWED_DOMAINS [ALLOWED_DOMAINS ...], --allowed-domains ALLOWED_DOMAINS [ALLOWED_DOMAINS ...]
                        List of domains that the spider is allowed to crawl
  -D, --debug           Enable debug output
  -O FILE, --output-document FILE
                        Write output to FILE instead of stdout

```
