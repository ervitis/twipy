# -*- coding: utf-8 -*-


HOME_TIME_LINE = '/statuses/home_timeline.json'
UPDATE_STATUS = '/statuses/update.json'
DM_READ = '/direct_messages.json'
DM_WRITE = '/direct_messages/new.json'
ME_READ = '/statuses/mentions_timeline.json'
FV_ADD = '/favorites/create.json'
FV_READ = '/favorites/list.json'
VERIFY_CREDENTIALS = '/account/verify_credentials.json'

TW_API_VERSION = '/1.1'
TW_HOST = 'https://api.twitter.com'


class DirectoryApi():

    def __init__(self):
        pass

    def get_url_home_timeline(self):
        pass

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
