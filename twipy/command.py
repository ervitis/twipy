# -*- coding: utf-8 -*-

from api import ApiTwip
from twipy import version
from adapter import Adapter, CliAdapter
import keys

COMMAND_HELP = """Command helps\n
-ht --home-timeline:\tGets the user's timeline
-v --version:\t\tPrints the version
"""

COMMAND_TIMELINE = ['-ht', '--home-timeline']
COMMAND_VERSION = ['-v', '--version']


class Command():

    def __init__(self, command):
        self._command = command
        self._api = ApiTwip(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
        self._adapter = Adapter()

    def dispatch(self):
        if self._command in COMMAND_TIMELINE:
            content = self._api.get_home_time_line()
            timeline = self._adapter.create_timeline_object(content)

            cli_adapter = CliAdapter(timeline)
            cli_adapter.get_statuses()

        elif self._command in COMMAND_VERSION:
            print version
        else:
            print COMMAND_HELP
