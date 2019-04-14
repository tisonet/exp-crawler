# -*- coding: utf-8 -*-
from urllib.parse import urlparse


class ParsedUrl(object):
    def __init__(self, url):
        self._url = url
        self._parsed = urlparse(url)

    @property
    def url(self):
        return self._url

    @property
    def domain(self):
        return self._parsed.netloc

    @property
    def path(self):
        return self._parsed.path
