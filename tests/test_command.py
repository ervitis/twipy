# -*- coding: utf-8 -*-

from unittest import TestCase
from twipy import command


class CommandTest(TestCase):

    def test_dispatch(self):
        arg = '-hola'
        comm = command.Command(command=arg)
        comm.dispatch()
