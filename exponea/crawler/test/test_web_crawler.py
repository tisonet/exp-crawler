# -*- coding: utf-8 -*-
import pytest
import mock
from exponea.crawler.web_crawler import WebCrawler
from exponea.crawler.downloader import Downloader
from exponea.crawler.storage import BlobStorage


@pytest.fixture()
def storage():
    return mock.create_autospec(BlobStorage)


@pytest.fixture()
def downloader():
    return mock.create_autospec(Downloader)


@pytest.fixture()
def crawler(storage, downloader):
    return WebCrawler('http://test.com', storage, downloader)


def test_crawler_when_no_images(crawler, downloader, storage):
    downloader.download.side_effect = ["<div></div>"]

    crawler.crawl()
    downloader.download.assert_called_with('http://test.com')
    storage.save_file.assert_not_called()


def test_crawler_save_downloaded_file(crawler, downloader, storage):
    downloader.download.side_effect = [
        "<img src='http://test.com/a.img'/>",
        "IMG_A_BLOB"
    ]

    crawler.crawl()
    downloader.download.assert_called_with('http://test.com/a.img')
    storage.save_file.assert_called_with(name='a.img', blob="IMG_A_BLOB")


def test_crawler_crawl_recursively(crawler, downloader, storage):
    downloader.download.side_effect = [
        "<a href='http://test.com/b.html'></a>",
        "<img src='http://test.com/b.img'/>",
        "IMG_B_BLOB"
    ]
    crawler.crawl()
    downloader.download.assert_called_with('http://test.com/b.img')
    storage.save_file.assert_called_with(name='b.img', blob="IMG_B_BLOB")


def test_crawler_download_image_once(crawler, downloader, storage):
    downloader.download.side_effect = [
        "<img src='http://test.com/a.img'/> <img src='http://test.com/a.img'/>",
        "IMG_A_BLOB"
    ]
    crawler.crawl()
    assert storage.save_file.call_count == 1


def test_crawler_crawle_nested_page_once(crawler, downloader, storage):
    downloader.download.side_effect = [
        "<a href='http://test.com/a.html'></a> <a href='http://test.com/a.html'></a> <a href='http://test.com/a.html'></a>",
        "<div></div>"
    ]
    crawler.crawl()
    assert downloader.download.call_count == 2


def test_get_name_from_url(crawler):
    assert crawler._get_name_from_url('test1') == 'test1'
    assert crawler._get_name_from_url('"http://exponea.com/a.img') == 'a.img'
    assert crawler._get_name_from_url('"https://exponea.com/img/b.img') == 'b.img'
