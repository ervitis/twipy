# -*- coding: utf-8 -*-

from twipy.keys import Keys, KeyFiles
from twipy.command import Command
import sys


def get_keys(keys):
    oauth_client = keys.get_auth_token()
    keys.get_token(oauth_client)
    oauth_client, pin_code = keys.authorize()
    keys.get_access(oauth_client, pin_code)


def first_time_storage():
    file_storage = KeyFiles()
    if not file_storage.exists_token_file():
        file_storage.create_folder()

    keys = Keys()

    if not file_storage.exists_token_file():
        get_keys(keys)
        keys.save_keys()


def main():
    c = ''

    first_time_storage()

    while c != 'q':
        c = raw_input('Command: ')
        command = Command(c)
        command.dispatch()

    exit(0)


if __name__ == '__main__':
    main()
