"""
A simple Pastebin API wrapper written in Python
Distributed under the MIT license AKA Do whatever you want with it
"""

import requests
from pb_lists import FORMATS, EXPIRES, PRIVACY

class PasteAPI:

    def __init__(self, dev_key, usr_key):
        self.dev_key = dev_key
        self.usr_key = usr_key
        
    def send_post(self, url, data):
        """ Responsible for converting data to utf8 and sending POST """
        if data:
            payload = {x: str(y).encode("utf-8") for x,y in data.items()}
        else:
            payload = None

        r = requests.post(url, data=payload)
        return r.text


    def create_user_key(self, dev_key, username, password):
        """ Create a new user key """
        payload = {
                    'api_dev_key': str(self.dev_key),
                    'api_user_name': str(username),
                    'api_user_password': str(password)
                  }

        return self.send_post("https://pastebin.com/api/api_login.php", payload)


    def get_user_info(self):
        """ Gets basic user information """
        payload = {
                   'api_option': 'userdetails',
                   'api_dev_key': str(self.dev_key),
                   'api_user_key': str(self.usr_key)
                  }

        return self.send_post('https://pastebin.com/api/api_post.php', payload)


    def create_paste(self, content, title=None, format=None, privacy=None, expire=None):
        """ 
            Create a new paste
            Optional params: usr_key, title, format, privacy, expire
            See pb_dicts.py for valid formats, expire times, and privacy settings 
        """
        payload = { 
                    'api_option': 'paste',
                    'api_dev_key': str(self.dev_key),
                    'api_paste_code': str(content),
                  }

        if self.usr_key:
            payload['api_user_key'] = self.usr_key
        if title:
            payload['api_paste_name'] = title
        if format and format in FORMATS:
            payload['api_paste_format'] = format
        if privacy and privacy in PRIVACY:
            payload['api_paste_private'] = privacy
        if expire and expire in EXPIRES:
            payload['api_paste_expire_date'] = expire
        
        return self.send_post("https://pastebin.com/api/api_post.php", payload)


    def delete_paste(self, paste_key):
        """ Deletes a specified paste """
        payload = { 
                    'api_option': 'delete',
                    'api_dev_key': str(self.dev_key),
                    'api_user_key': str(self.usr_key),
                    'api_paste_key': str(paste_key)
                  }

        return self.send_post("https://pastebin.com/api/api_post.php", payload)


    def get_user_raw_paste(self, paste_key):
        """ Get raw paste data from pastes belonging to user only """
        payload = {
                   'api_option': 'show_paste',
                   'api_dev_key': str(self.dev_key),
                   'api_user_key': str(self.usr_key),
                   'api_paste_key': str(paste_key)
                  }

        return self.send_post('https://pastebin.com/api/api_raw.php', payload)


    def get_raw_paste(self, paste_key):
        """ Get raw paste data from any paste """
        return self.send_post('https://pastebin.com/raw/' + str(paste_key), None)


    def list_user_pastes(self, limit=None):
        """ 
            List pastes made by the user 
            Optional param: limit 
        """
        payload = {
                   'api_option': 'list',
                   'api_dev_key': str(self.dev_key),
                   'api_user_key': str(self.usr_key)
                  }

        if limit:
            payload['api_results_limit'] = limit

        return self.send_post("https://pastebin.com/api/api_post.php", data=payload)


    def list_trending_pastes(self):
        """ List trending pastes """
        payload = {
                   'api_option': 'trends',
                   'api_dev_key': str(self.dev_key)
                  }

        return self.send_post('https://pastebin.com/api/api_post.php', payload)
