# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name='exponea-crawler',
      version='1.0',
      description='Exponea image crawler',
      author='Zdenek Tison',
      author_email='zdenek.tison@gmail.com',
      packages=['exponea'],
      scripts=['exponea_crawler.py'],
      install_requires=[
          'pytest',
          'mock',
          'beautifulsoup4'
      ]
  )
