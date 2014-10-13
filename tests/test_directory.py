# -*- coding: utf-8 -*-

from twipy.directory import DirectoryApi
from twipy import directory
from unittest import TestCase


class DirectoryTest(TestCase):

    def test_constants(self):
        self.assertTrue(isinstance(directory.ACCESS_TOKEN, str))
        self.assertTrue(isinstance(directory.AUTHORIZE_URL, str))
        self.assertTrue(isinstance(directory.DM_READ, str))
        self.assertTrue(isinstance(directory.DM_WRITE, str))
        self.assertTrue(isinstance(directory.FV_ADD, str))
        self.assertTrue(isinstance(directory.FV_READ, str))
        self.assertTrue(isinstance(directory.HOME_TIME_LINE, str))
        self.assertTrue(isinstance(directory.ME_READ, str))
        self.assertTrue(isinstance(directory.REQUEST_TOKEN, str))
        self.assertTrue(isinstance(directory.TW_API_VERSION, str))
        self.assertTrue(isinstance(directory.TWITTER_URL, str))
        self.assertTrue(isinstance(directory.UPDATE_STATUS, str))
        self.assertTrue(isinstance(directory.VERIFY_CREDENTIALS, str))

    def test_directory(self):
        directory_api = DirectoryApi()

        self.assertTrue(isinstance(directory_api.get_url_home_timeline(), str))
        self.assertTrue(isinstance(directory_api.get_url_request_token(), str))
        self.assertTrue(isinstance(directory_api.get_url_authorize_url(), str))
        self.assertTrue(isinstance(directory_api.get_url_access_token(), str))
        self.assertTrue(isinstance(directory_api.get_url_update_status(), str))
        self.assertTrue(isinstance(directory_api.get_url_send_dm(), str))
        self.assertTrue(isinstance(directory_api.get_url_read_dm(), str))
        self.assertTrue(isinstance(directory_api.get_url_read_mentions(), str))
        self.assertTrue(isinstance(directory_api.get_url_new_fav(), str))
        self.assertTrue(isinstance(directory_api.get_url_read_favs(), str))
        self.assertTrue(isinstance(directory_api.get_url_verify_credentials(), str))
