# -*- coding: utf-8 -*-
"""
- Slack
- Hipchat
- Chatwork
- Skype
- LINE
- Fluentd
- Facebook
- Goolge Chat
- Lingr
- Email
- Twitter
- Github Issues
- Butbicket Issues
- Redmine Issues
- Pastebin
- Errbit
"""
import json
import logging

import requests
import zope.dottedname.resolve
from zope.interface import (
    implementer,
    Interface,
    )


class SlackIncomingWebHookSender(object):
    api_url = 'https://{}/services/hooks/incoming-webhook?token={}'

    def __init__(self, domain, token, channel, username, icon_emoji=':gohst'):
        self._url = self.api_url.format(domain, token)
        self._channel = channel
        self._username = username
        self._icon_emoji = icon_emoji

    def connect(self):
        pass

    def build(self, msg):
        return json.dumps({
            'channel': self._channel,
            'username': self._username,
            'icon_emoji': self._icon_emoji,
            'text': msg,
            })

    def send(self, msg):
        req = self.build(msg)
        return requests.post(self._url, req, verify=False)

    def close(self):
        pass


class LogCollectionHandler(logging.Handler):
    def __init__(self, level, sender_name, *args, **kwds):
        super(LogCollectionHandler, self).__init__(level)
        self._sender_name = sender_name
        self._args = args
        self._kwds = kwds
        self._conn = None
        self.connect()

    def connect(self):
        if not self._conn:
            klass = zope.dottedname.resolve.resolve(self._sender_name)
            self._conn = klass(*self._args, **self._kwds)
        self._conn.connect()

    def emit(self, record):
        msg = self.format(record)
        self._conn.send(msg)

    def close(self):
        self.aquire()
        try:
            self._conn.close()
            super(LogCollectionHandler, self).close()
        finally:
            self.release()
