# -*- coding: utf-8 -*-

from unittest import TestCase
import tests
from twipy.keys import Keys
from oauth2 import Client


class KeysTest(TestCase):

    def test_keys(self):
        k = tests.create_keys()

        self.assertTrue(isinstance(k, Keys))

        oauth = k.get_auth_token()
        self.assertTrue(isinstance(oauth, Client))

        c, cs = k.get_consumer_keys
        self.assertTrue(isinstance(c, str))
        self.assertGreater(len(c), 0)
        self.assertTrue(isinstance(cs, str))
        self.assertGreater(len(cs), 0)
