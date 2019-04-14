# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import logging

logger = logging.getLogger()


class Downloader(object):
    def download(self, url):
        raise NotImplementedError()


class SyncDownloader(Downloader):

    def download(self, url):
        try:

            response = urlopen(url)
            return response.read()

        except HTTPError as e:
            logger.warning("Http error {} when downloading url: {}".format(url, e.code))

        except URLError as e:
            logger.warning("Can't download url: {} because: {}".format(url, e.reason))

        except Exception as e:
            logger.warning("Can't download url: {} because: {}".format(url, e))

        return None
