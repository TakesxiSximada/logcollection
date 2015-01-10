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


class SlackAPIChatPostMessageSender(object):
    api_url = 'https://slack.com/api/chat.postMessage'

    def __init__(self, token, channel, username, icon_emoji=':gohst'):
        self._token = token
        self._url = self.api_url
        self._channel = channel
        self._username = username
        self._icon_emoji = icon_emoji

    def connect(self):
        pass

    def build(self, msg):
        return {
            'token': self._token,
            'channel': self._channel,
            'username': self._username,
            'icon_emoji': self._icon_emoji,
            'text': msg,
            }

    def send(self, msg):
        params = self.build(msg)
        return requests.post(self._url, params=params, verify=False)

    def close(self):
        pass


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


class HipChatSender(object):
    def __init__(self,
                 room_id,
                 token,
                 timeout=10,
                 notify=0,
                 message_format='text',
                 api='rooms/messages',
                 method='POST',
                 ):
        self._api = api
        self._method = method
        self._timeout = timeout
        self._notify = notify
        self._conn = None

    def connect(self):
        import hipchat
        if not self._conn:
            self._conn = hipchat.HipChat(token=self._token)

    def build(self, msg):
        return {
            'room_id': self._room_id,
            'from': 'dummy',
            'message': msg,
            'message_format': self._message_format,
            'notify': self._notify,
            }

    def send(self, msg):
        req = self.build(msg)
        return self._conn.method(
            self._api,
            self._method,
            req,
            timetout=self._timetout,
            )

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
