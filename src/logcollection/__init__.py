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
import zope.dottedname
from zope.interface import (
    implementer,
    Interface,
    )

import hipchat
import fluent.handler


class ISender(Interface):
    def connect(self):
        pass

    def close(self):
        pass

    def emit_with_time(self, label, timestamp, data):
        pass


class Handler(object):
    pass


# class IHandler(Interface):
#     def build_message(self, record):
#         """送信するためのメッセージを作成する
#         """
#         pass

#     def send_message(self, msg):
#         """メッセージを送信する
#         """
#         pass


# @implementer(IHandler)
# class BaseHandler(logging.Handler):
#     def emit(self, record):
#         try:
#             msg = self.build_message(record)
#             self.send_message(msg)
#         except (KeyboardInterrupt, SystemExit):
#             raise
#         except:
#             self.handleError(record)

#     def build_message(self, record):
#         return self.format(record)

#     def send_message(self, msg):
#         raise NotImplementedError()


# @implementer(IHandler)
# class SlackHandler(BaseHandler):
#     """Slack logging handler using incoming webhook.
#     """
#     def __init__(self, url, channel, username, icon=':gohst'):
#         super(HipchatHandler, self).__init__()
#         self._url = url
#         self._channel = channel
#         self._username = username
#         self._iconx = icon

#     def build_message(self, record):
#         text = self.format(record)
#         return json.dumps({
#             'text': text,
#             'channel': self._channel,
#             'username': self._username,
#             'icon_emoji': self._icon,
#             })

#     def send_message(self, msg):
#         return requests.post(self._url, data=msg, verify=False)


# @implementer(IHandler)
# class HipchatHandler(BaseHandler):
#     def __init__(self, token, timeout=10, fmt='text', notify=True):
#         super(HipchatHandler, self).__init__()
#         self._conn = hipchat.HipChat(token=token)
#         self._tiemout = int(timeout)
#         self._fmt = fmt
#         self._notify = notify

#     def build_message(self, record):
#         text = self.format(record)
#         color = ''
#         if record.levelno >= logging.WARN:
#             color = 'yellow'
#         if record.levelno >= logging.ERROR:
#             color = 'red'

#         return {
#             'message': text,
#             'room_id': self._room_id,
#             'from': record.name,
#             'message_format': self._fmt,
#             'notify': self._notify,
#             'color': color,
#             }

#     def send_message(self, msg):
#         return self._conn.method(
#             'rooms/message', 'POST', msg, timeout=self._timeout)


# class FluentHandler(fluent.handers.FluentHandler):
#     pass
