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


def test_crawler_save_downloaded_file(crawler, downloader, storage):
    downloader.download.return_value = "<img src='http://test.com/a.img'>"

    crawler.crawl()

    storage.save_file.assert_called_with(name='a.img', blob="<img src='http://test.com/a.img'>")


def test_get_name_from_url(crawler):
    assert crawler._get_name_from_url('test1') == 'test1'
    assert crawler._get_name_from_url('"http://exponea.com/a.img') == 'a.img'
    assert crawler._get_name_from_url('"https://exponea.com/img/b.img') == 'b.img'
