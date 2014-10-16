# -*- coding: utf-8 -*-

from twipy.adapter import Adapter, CliAdapter
from twipy.models import Timeline
import tests
from unittest import TestCase


class TestAdapter(TestCase):

    def test_create_timeline_object(self):
        api_twipy = tests.create_api()
        content = api_twipy.get_home_time_line()

        adapter = Adapter()
        timeline = adapter.create_timeline_object(content)

        self.assertTrue(isinstance(timeline, Timeline))
        self.assertGreater(len(timeline.statuses), 0)


class TestCliAdapter(TestCase):

    def test_cli_adapter(self):
        api_twipy = tests.create_api()
        content = api_twipy.get_home_time_line()

        adapter = Adapter()
        timeline = adapter.create_timeline_object(content)

        cli_adapter = CliAdapter(timeline)

        self.assertTrue(isinstance(cli_adapter, CliAdapter))
