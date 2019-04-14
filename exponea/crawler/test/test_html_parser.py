# -*- coding: utf-8 -*-
import pytest

from ..html_parser import HtmlParser


def test_get_images_when_https():
    parser = HtmlParser('<div><img src="https://exponea.com/a.img"></img></div>')
    assert list(parser.get_images_urls()) == ['https://exponea.com/a.img']


def test_get_images_when_http():
    parser = HtmlParser('<div><img src="http://exponea.com/a.img"></img></div>')
    assert list(parser.get_images_urls()) == ['http://exponea.com/a.img']


def test_get_links_when_http():
    parser = HtmlParser('<div><a href="http://exponea.com/page2.html"></a></div>')
    assert list(parser.get_links_urls()) == ['http://exponea.com/page2.html']