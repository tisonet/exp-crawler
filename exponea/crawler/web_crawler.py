# -*- coding: utf-8 -*-
from exponea.crawler.html_parser import HtmlParser
from exponea.crawler.parsed_url import ParsedUrl
import logging

logger = logging.getLogger()


class WebCrawler(object):
    def __init__(self, root_page_url, blob_storage, downloader):
        self._root_page_url = ParsedUrl(root_page_url)
        self._downloader = downloader
        self._blob_storage = blob_storage
        self._downloaded_images = set()
        self._crawled_paths = set()

    def crawl(self):
        logger.info('Web crawler started for web: {}'.format(self._root_page_url.url))

        self._crawl_recursively([self._root_page_url])

        logger.info('Web crawler finished, successfully crawled {} images'.format(len(self._downloaded_images)))

    def _crawl_recursively(self, urls):

        for parsed_url in urls:
            if parsed_url.path not in self._crawled_paths:

                logger.info('Crawling url: {}'.format(parsed_url.url))
                self._crawled_paths.add(parsed_url.path)

                page_data = self._downloader.download(parsed_url.url)
                if page_data:
                    parsed_page = HtmlParser(page_data)

                    nested_urls = self._get_nested_urls_to_crawl(parsed_page.get_links_urls())

                    self._download_images(parsed_page.get_images_urls())
                    self._crawl_recursively(nested_urls)

                logger.info('Url: {} crawled'.format(parsed_url.url))

    def _download_images(self, images):
        for img_url in images:
            if img_url not in self._downloaded_images:
                self._downloaded_images.add(img_url)

                img_data = self._downloader.download(img_url)
                if img_data:
                    self._blob_storage.save_file(self._get_name_from_url(img_url), img_data)
                else:
                    logger.info('Invalid image url: {}, skipping'.format(img_url))

    def _get_nested_urls_to_crawl(self, page_links):
        nested_urls = set()

        for link in page_links:
            parsed_link_url = ParsedUrl(link)
            if parsed_link_url.domain == self._root_page_url.domain and parsed_link_url.path not in self._crawled_paths:
                nested_urls.add(parsed_link_url)

        return nested_urls

    @staticmethod
    def _get_name_from_url(image_url):
        return image_url.split('/')[-1]

