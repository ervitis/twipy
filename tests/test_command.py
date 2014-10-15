# -*- coding: utf-8 -*-

from unittest import TestCase
from twipy import command


class CommandTest(TestCase):

    def test_command(self):
        c = '-help'
        com = command.Command(c)
        com.dispatch()
