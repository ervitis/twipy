from twipy.models import Status, User, DirectMessage, Timeline
from twipy.api import ApiTwip
from twipy import keys
from cStringIO import StringIO
import sys

from datetime import datetime


def create_status():
    return Status(created_at=datetime.now(), id_str='1', text='Prueba test', user='botty')


def create_another_status():
    return Status(created_at=datetime.now(), id_str='3', text='Prueba test2', user='botty2')


def create_user():
    return User(
        created_at=datetime.now(),
        description='bot test',
        favourites_count=2,
        followers_count=10,
        friends_count=3,
        id_str='1',
        name='bot',
        screen_name='bot_screen',
        url='http://prueba.es')


def create_dm():
    return DirectMessage(
        created_at=datetime.now(),
        id_str='3',
        text='DM prueba',
        recipient_screen_name='bot_screen',
        sender_screen_name='bot_sender')


def create_timeline():
    return Timeline()


def create_api():
    return ApiTwip(consumer_key=keys.CONSUMER_KEY, consumer_secret=keys.CONSUMER_SECRET)


class Capturing(str):

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._stdout
