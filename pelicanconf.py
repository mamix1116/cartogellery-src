#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'mamix'
SITENAME = 'Civic Carto Gallery'
SITEURL = SITEURL_ABS = ''

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

PATH = 'content'
THEME = 'themes/html5-dopetrope'

TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ja': '%Y-%m-%d(%a)',
}

DEFAULT_LANG = 'ja'

SUMMARY_MAX_LENGTH = 100

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 50

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# additional setting for Theme html5-dopetrope
ABOUT_TEXT = 'オープンデータなどを利用して作成されたWEB地図を集めたギャラリーサイト'
ABOUT_IMAGE = ''
COPYRIGHT = 'mamix'
