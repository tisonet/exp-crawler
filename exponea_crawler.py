#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from exponea.crawler.web_crawler import WebCrawler
from exponea.crawler.storage import BlobFileStorage
from exponea.crawler.downloader import SyncDownloader

logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    storage = BlobFileStorage('/tmp/exponea/')
    downloader = SyncDownloader()
    crawler = WebCrawler('https://exponea.com/', blob_storage=storage, downloader=downloader)
    crawler.crawl()

