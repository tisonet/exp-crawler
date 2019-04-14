# -*- coding: utf-8 -*-
import os
import logging

logger = logging.getLogger(__name__)


class BlobStorage(object):
    def save_file(self, name, blob):
        raise NotImplementedError()


class BlobFileStorage(BlobStorage):
    def __init__(self, storage_dir):
        self._storage_dir = storage_dir
        self._create_storage_dir()

    def save_file(self, name, blob):
        try:
            file_path = os.path.join(self._storage_dir, name)
            with open(file_path, 'wb') as f:
                f.write(blob)
        except Exception:
            logger.exception('Cant write file {} to dir: {}'.format(name, self._storage_dir))
            raise

    def _create_storage_dir(self):
        try:
            if not os.path.isdir(self._storage_dir):
                os.makedirs(self._storage_dir, exist_ok=True)
        except Exception:
            logger.exception('Cant create storage dir: {]'.format(self._storage_dir))
            raise
