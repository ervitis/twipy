# -*- coding: utf-8 -*-

from unittest import TestCase
import tests


LONG_TEXT = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
"""

SHORT_TEXT = ' Travis rocks! And it\'s very cool and free '

LINK = ' https://www.youtube.com/watch?v=dQw4w9WgXcQ '


class TestApi(TestCase):

    def test_consumer_keys(self):
        api_twipy = tests.create_api()

        self.assertTrue(isinstance(api_twipy._consumer_key, str))
        self.assertTrue(isinstance(api_twipy._consumer_secret, str))

    def test_get_home_timeline(self):
        api_twipy = tests.create_api()

        content = api_twipy.get_home_time_line()
        self.assertTrue(isinstance(content, str))
        self.assertGreater(len(content), 0)

    def test_exception_consumer_keys(self):
        self.assertRaises(ValueError, api_twipy=tests.create_api_without_consumer_key())

    def test_update_status(self):
        api_twipy = tests.create_api()

        api_twipy.update_status(text=SHORT_TEXT)
        api_twipy.update_status(text=LONG_TEXT)
        api_twipy.update_status(text=SHORT_TEXT + LINK + SHORT_TEXT)

    def test_send_direct_message(self):
        api_twipy = tests.create_api()

        api_twipy.send_direct_message()

    def test_get_direct_messages(self):
        api_twipy = tests.create_api()

        api_twipy.get_direct_messages()

    def test_get_mentions(self):
        api_twipy = tests.create_api()

        api_twipy.get_mentions()

    def test_get_favs(self):
        api_twipy = tests.create_api()

        api_twipy.get_favs()

    def test_verify_credentials(self):
        api_twipy = tests.create_api()

        api_twipy.verify_credentials()

    def test_create_fav(self):
        api_twipy = tests.create_api()

        api_twipy.create_fav()
