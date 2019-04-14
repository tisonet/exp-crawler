# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def __init__(self, html):
        self._soup = BeautifulSoup(html, 'html.parser')
        self._valid_links_regex = re.compile("^http(s)?://")

    def get_images_urls(self):
        return {img.get('src') for img in self._soup.findAll('img', {'src': self._valid_links_regex})}

    def get_links_urls(self):
        return {img.get('href') for img in self._soup.findAll('a', {'href': self._valid_links_regex})}
