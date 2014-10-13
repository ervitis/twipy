# -*- coding: utf-8 -*-

import tests
from unittest import TestCase
from twipy.models import Status, User, DirectMessage, Timeline


class ObjectsTest(TestCase):

    def test_status(self):
        status = tests.create_status()
        self.assertTrue(isinstance(status, Status))
        self.assertFalse(isinstance(status, User))
        self.assertFalse(isinstance(status, DirectMessage))
        self.assertEqual(status.__str__(), status.id_str)

    def test_dm(self):
        dm = tests.create_dm()
        self.assertFalse(isinstance(dm, Status))
        self.assertFalse(isinstance(dm, User))
        self.assertTrue(isinstance(dm, DirectMessage))
        self.assertEqual(dm.__str__(), dm.id_str)

    def test_user(self):
        user = tests.create_user()
        self.assertFalse(isinstance(user, Status))
        self.assertTrue(isinstance(user, User))
        self.assertFalse(isinstance(user, DirectMessage))
        self.assertEqual(user.__str__(), user.id_str)


class TimelineTest(TestCase):

    def test_timeline(self):
        timeline = tests.create_timeline()

        self.assertTrue(isinstance(timeline, Timeline))
        self.assertEqual(0, len(timeline.statuses))

        status = None
        with self.assertRaises(Exception):
            timeline.add(status)

        status2 = tests.create_another_status()
        self.assertRaises(ValueError, timeline.remove(status2))

        status = tests.create_status()
        timeline.add(status)
        self.assertEqual(1, len(timeline.statuses))

        timeline.remove(status)
        self.assertEqual(0, len(timeline.statuses))
