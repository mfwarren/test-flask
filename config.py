# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True
SECRET_KEY = 'iwu8nx490t8w3on8fg7w94875yfwo378yfj0qs78934tfn8o7w3g4fn0q87g'


OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}]


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

WHOOSH_BASE = os.path.join(basedir, 'search.db')

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['me@example.com']


LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}
