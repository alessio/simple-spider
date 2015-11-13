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
python crawler.py -h
