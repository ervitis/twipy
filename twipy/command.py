# -*- coding: utf-8 -*-

from api import ApiTwip
from twipy import version
from adapter import Adapter, CliAdapter
import keys

COMMAND_HELP_TEXT = """Command helps\n
ht:\tGets the user's timeline
v:\tPrints the version
h:\tPrints help commands
u:\tWrite u <text> to update the Twitter status
"""

COMMAND_TIMELINE = ['ht']
COMMAND_VERSION = ['v']
COMMAND_EXIT = ['q']
COMMAND_HELP = ['h']
COMMAND_UPDATE = ['u']


class Command():

    def __init__(self, command):
        self._command = command
        self._api = ApiTwip(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
        self._adapter = Adapter()

    def dispatch(self):
        if self._command in COMMAND_TIMELINE:
            content = self._api.get_home_time_line()  # pragma: no cover
            timeline = self._adapter.create_timeline_object(content)  # pragma: no cover

            cli_adapter = CliAdapter(timeline)  # pragma: no cover
            cli_adapter.get_statuses()  # pragma: no cover

        elif self._command in COMMAND_VERSION:
            print version  # pragma: no cover

        elif self._command in COMMAND_EXIT:
            pass  # pragma: no cover

        elif self._command in COMMAND_HELP:
            print COMMAND_HELP_TEXT  # pragma: no cover

        elif len(self._command) > 2:
            com = self._command[:2].strip()
            text = self._command[2:]
            self._send_info(com, text)

        else:
            print COMMAND_HELP_TEXT

    def _send_info(self, com, text):
        if com in COMMAND_UPDATE:
            self._api.update_status(text)
