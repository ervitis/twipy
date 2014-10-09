# -*- coding: utf-8 -*-

from twipy.keys import Keys, KeyFiles


def get_keys(keys):
    oauth_client = keys.get_auth_token()
    keys.get_token(oauth_client)
    oauth_client, pin_code = keys.authorize()
    keys.get_access(oauth_client, pin_code)


def main():
    get_version()
    file_storage = KeyFiles()
    file_storage.create_folder()

    keys = Keys()

    if not file_storage.exists_token_file():
        get_keys(keys)

        keys.save_keys()

    exit(0)


if __name__ == '__main__':
    main()
