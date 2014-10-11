# -*- coding: utf-8 -*-

from twipy.keys import Keys, KeyFiles
from twipy.command import Command
import sys


def get_keys(keys):
    oauth_client = keys.get_auth_token()
    keys.get_token(oauth_client)
    oauth_client, pin_code = keys.authorize()
    keys.get_access(oauth_client, pin_code)


def is_first_time_storage():
    file_storage = KeyFiles()
    file_storage.create_folder()

    keys = Keys()

    if not file_storage.exists_token_file():
        get_keys(keys)
        keys.save_keys()

        return True
    return False


def main():
    if len(sys.argv) != 2:
        raise Exception('Too or less arguments\nExample: main.py <argument>')

    if not is_first_time_storage():
        command = Command(sys.argv[1])
        command.dispatch()
    else:
        print 'Execute again the program normally'

    exit(0)


if __name__ == '__main__':
    main()
