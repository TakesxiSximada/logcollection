# -*- coding: utf-8 -*-
"""
- Slack -> ok
- Hipchat -> ok
- Chatwork
- Skype
- LINE
- Fluentd -> ok
- Facebook
- Goolge Chat
- Lingr
- Email
- Twitter
- Github Issues
- Butbicket Issues
- Redmine Issues -> ok
- Pastebin
- Errbit
"""
import json
import logging

import requests
import zope.dottedname.resolve
import zope.interface
from zope.interface import (
    implementer,
    Interface,
    )


class LogCollectionHandler(logging.Handler):
    def __init__(self, sender_name, *args, **kwds):
        super(LogCollectionHandler, self).__init__()
        self._sender_name = sender_name
        self._args = args
        self._kwds = kwds
        self._conn = None
        self.connect()

    def connect(self):
        if not self._conn:
            klass = key_sender.get(self._sender_name, None) or \
                zope.dottedname.resolve.resolve(self._sender_name)
            self._conn = klass(*self._args, **self._kwds)
        self._conn.connect()

    def emit(self, record):
        msg = self.format(record)
        self._conn.send(msg, record)

    def close(self):
        self.aquire()
        try:
            self._conn.close()
            super(LogCollectionHandler, self).close()
        finally:
            self.release()
