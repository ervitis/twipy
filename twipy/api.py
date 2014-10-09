# -*- coding: utf-8 -*-

import oauth2


class ApiTwip(object):
    """
    Api class
    """

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 oauth_token,
                 oauth_token_secret):

        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._oauth_token = oauth_token
        self._oauth_token_secret = oauth_token_secret
        self.is_authenticated = False
        self._client = None

    def _authenticate(self):
        if not self._client:
            self._client = self._get_client()
            self.is_authenticated = True

    def _get_client(self):
        try:
            consumer = oauth2.Consumer(key=self._consumer_key, secret=self._consumer_secret)
            access_token = oauth2.Token(key=self._oauth_token, secret=self._oauth_token_secret)
            client = oauth2.Client(consumer=consumer, token=access_token)
        except ValueError as e:
            raise Exception(e.message)

        # client object. To access the TW API: client.request(url)
        return client

    def update_status(self):
        pass

    def send_direct_message(self):
        pass

    def get_home_time_line(self):
        pass

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
