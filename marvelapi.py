# -*- coding: utf-8 -*-
#description: Consumes the MARVEL API
#author: Arianne S. Silva
#create: 20/12/2020

import requests
from time import time
from hashlib import md5

class Marvel(object):
    def __init__(self, api_key, private_key):
        self.private_key = private_key
        self.api_key = api_key

    def get(self, resource, kwargs):
        url = 'http://gateway.marvel.com/v1/public'
        #checks if ID has enter
        if 'id' in kwargs:
            if resource == 'characters':
                url += '/characters/%s' % (kwargs['id'])
            else:
                url += '/characters/%s/%s' % (kwargs['id'], resource)
            kwargs.pop('id')
        else:
            url += '/%s' % resource
        headers = {'Accept': '*/*'}
        timestamp = str(time())
        hash_keys = md5(timestamp.encode('UTF-8') + self.private_key.encode('UTF-8') + self.api_key.encode('UTF-8'))
        kwargs.update({'apikey': self.api_key.encode('UTF-8'), 'ts': timestamp, 'hash': hash_keys.hexdigest()})
        #self._show_attributes(url=url, params=kwargs)
        try:
            result = requests.get(url, params=kwargs, headers=headers)
        except Exception as erro:
            print("Connection error. Cannot to connect with API MARVEL.")
            print("Check your network connection and try again.")
            print("")
            return None
        return result

    #shows the chosen attributes
    def _show_attributes(self, url, params):
        print("endpoint : ", url)
        for key, value in params.items():
            if (key == 'ts') or (key == 'hash'):
                continue
            print(key, " : ", value)
        print("")
        return

    def characters(self, **kwargs):
        return (self.get('characters', kwargs))

    def comics(self, **kwargs):
        return (self.get('comics', kwargs))

    def events(self, **kwargs):
        return (self.get('events', kwargs))

    def stories(self, **kwargs):
        return (self.get('stories', kwargs))

    def series(self, **kwargs):
        return (self.get('series', kwargs))


