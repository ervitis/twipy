# -*- coding: utf-8 -*-

from api import ApiTwip
from twipy import version
from adapter import Adapter, CliAdapter
import keys
import re

COMMAND_HELP_TEXT = """Command helps\n
ht:\tGets the user's timeline
v:\tPrints the version
h:\tPrints help commands
u:\tWrite u <text> to update your status
rp:\tWrite rp <id_number> <text> to reply a status. The <id_number> is between 0 and 19.
\tDon't forget to include the user name with the '@'
q:\tExits
"""

COMMAND_TIMELINE = ['ht']
COMMAND_VERSION = ['v']
COMMAND_EXIT = ['q']
COMMAND_HELP = ['h']
COMMAND_UPDATE = ['u']
COMMAND_REPLY = ['rp']

REG_EXP_COMMAND_RP = '[^0-9]{1,2}'


class Command():

    def __init__(self):
        self._command = None
        self._api = ApiTwip(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
        self._adapter = Adapter()
        self._timeline = None

    def dispatch(self, command):
        self._command = command

        if self._command in COMMAND_TIMELINE:
            content = self._api.get_home_time_line()  # pragma: no cover
            self._timeline = self._adapter.create_timeline_object(content)  # pragma: no cover

            cli_adapter = CliAdapter(self._timeline)  # pragma: no cover
            cli_adapter.get_statuses()  # pragma: no cover

        elif self._command in COMMAND_VERSION:
            print version  # pragma: no cover

        elif self._command in COMMAND_EXIT:
            pass  # pragma: no cover

        elif self._command in COMMAND_HELP:
            print COMMAND_HELP_TEXT  # pragma: no cover

        elif len(self._command) > 2:
            com = self._command[:2].strip()
            text = self._command[2:].strip()
            self._send_info(com, text)

        else:
            print COMMAND_HELP_TEXT

    def _send_info(self, com, text):
        if com in COMMAND_UPDATE:
            self._api.update_status(text)

        elif com in COMMAND_REPLY:
            if not self._timeline:
                print 'Timeline is empty. Execute first the ht command'
                return

            cli_adapter = CliAdapter(self._timeline)

            c_id = text[:2].strip()
            text = text[2:]
            r = re.findall(REG_EXP_COMMAND_RP, c_id)
            if r:
                print 'Bad reply id. Only numbers between 0 and 19'
                return

            c_id = int(c_id)
            if c_id < 0 or c_id > 19:
                print 'Bad reply id. Range: 0..19'
                return

            status = cli_adapter.get_status_from_id(c_id)
            self._api.update_status(text=text, reply_to=status.id_str)
