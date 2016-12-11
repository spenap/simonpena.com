#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import calendar

AUTHOR = u'Sim\xf3n'
SITENAME = u'simonpena.com'
SITEURL = '/blog'
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/notmyidea'

SITESUBTITLE = 'Una mezcla heterogénea de tecnología y desvaríos'

GITHUB_URL = ''
TWITTER_USERNAME = 'spenap'

DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (('Home', '/'), ('Archives', '/articles'), ('Categories', '/categories'), ('Tags', '/tags'))

# location of the per-section indices
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories/index.html'
TAGS_SAVE_AS = 'tags/index.html'

# articles have the date in their URL
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# whereas pages do not
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# archives are supersets of the articles
ARCHIVES_SAVE_AS = 'articles/index.html'
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/index.html'

# sub-pages for each section
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud']

TAG_CLOUD_BADGE = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_MAX_ITEMS = 40

def month_name_filter(month_number):
	return calendar.month_name[month_number]

JINJA_FILTERS = { 'month_name': month_name_filter }
