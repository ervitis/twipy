# -*- coding: utf-8 -*-

from urlparse import urljoin

HOME_TIME_LINE = '/statuses/home_timeline.json'
UPDATE_STATUS = '/statuses/update.json'
DM_READ = '/direct_messages.json'
DM_WRITE = '/direct_messages/new.json'
ME_READ = '/statuses/mentions_timeline.json'
FV_ADD = '/favorites/create.json'
FV_READ = '/favorites/list.json'
VERIFY_CREDENTIALS = '/account/verify_credentials.json'

REQUEST_TOKEN = '/oauth/request_token'
AUTHORIZE_URL = '/oauth/authorize'
ACCESS_TOKEN = 'oauth/access_token'

TWITTER_URL = 'https://api.twitter.com'
TW_API_VERSION = '/1.1'


class DirectoryApi():

    def __init__(self):
        self._url = None
        self._twitter_api = urljoin(TWITTER_URL, TW_API_VERSION)

    def get_url_home_timeline(self):
        self._url = self._twitter_api + HOME_TIME_LINE
        return self._url

    def get_url_update_status(self):
        pass

    def get_url_send_dm(self):
        pass

    def get_url_read_dm(self):
        pass

    def get_url_read_mentions(self):
        pass

    def get_url_new_fav(self):
        pass

    def get_url_read_favs(self):
        pass

    def get_url_verify_credentials(self):
        pass

    def get_url_request_token(self):
        self._url = urljoin(TWITTER_URL, REQUEST_TOKEN)
        return self._url

    def get_url_authorize_url(self):
        self._url = urljoin(TWITTER_URL, AUTHORIZE_URL)
        return self._url

    def get_url_access_token(self):
        self._url = urljoin(TWITTER_URL, ACCESS_TOKEN)
        return self._url
