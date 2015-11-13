from setuptools import setup

setup(
    name="simple-spider",
    version="0.0.1",
    author="Alessio Treglia",
    author_email="quadrispro@ubuntu.com",
    install_requires=[
        "Scrapy>=1.0.3",
    ],
    scripts=["crawler.py"],
    test_suite="tests",
)
