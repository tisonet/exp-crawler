# -*- coding: utf-8 -*-
from exponea.crawler.parsed_url import ParsedUrl


def test_parse_url():
    parsed = ParsedUrl('http://exponea.com/blog/a.html')
    assert parsed.domain == 'exponea.com'
    assert parsed.path == '/blog/a.html'
    assert parsed.url == 'http://exponea.com/blog/a.html'