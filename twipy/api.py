# -*- coding: utf-8 -*-

import oauth2

from directory import DirectoryApi
from keys import KeyFiles


RESPONSE_OK = 200


class ApiTwip(object):
    """
    Api class
    """

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 oauth_token=None,
                 oauth_token_secret=None):

        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._oauth_token = oauth_token
        self._oauth_token_secret = oauth_token_secret
        self.is_authenticated = False
        self._client = None
        self._directory_api = DirectoryApi()

    def _authenticate(self):
        if not self._client:
            key_files = KeyFiles()

            if not self._oauth_token:
                self._oauth_token, self._oauth_token_secret = key_files.open_token_file() # pragma: no cover

            self._client = self._get_client()
            self.is_authenticated = True

    def _get_client(self):
        try:
            consumer = oauth2.Consumer(key=self._consumer_key, secret=self._consumer_secret)
            access_token = oauth2.Token(key=self._oauth_token, secret=self._oauth_token_secret)
            client = oauth2.Client(consumer=consumer, token=access_token)
        except ValueError as e:  # pragma: no cover
            raise Exception(e.message)  # pragma: no cover

        # client object. To access the TW API: client.request(url)
        return client

    def update_status(self):
        pass

    def send_direct_message(self):
        pass

    def get_home_time_line(self):
        if not self.is_authenticated:
            self._authenticate()
        uri = self._directory_api.get_url_home_timeline()

        response, content = self._client.request(uri=uri)
        response_status = is_response_ok(response)

        if not response_status:
            raise Exception('Response not ok %s' % response_status)  # pragma: no cover

        return content

    def get_direct_messages(self):
        pass

    def get_mentions(self):
        pass

    def create_fav(self):
        pass

    def get_favs(self):
        pass

    def verify_credentials(self):
        pass


def is_response_ok(response):
    response_status = int(response['status'])

    if response_status == RESPONSE_OK:
        return True
    return response_status  # pragma: no cover
