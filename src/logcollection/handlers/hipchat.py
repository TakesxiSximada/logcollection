# -*- codiing: utf-8 -*-
import hipchat


class HipChatSender(object):
    def __init__(self,
                 token,
                 room_id,
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
        if not self._conn:
            self._conn = hipchat.HipChat(token=self._token)

    def build(self, msg, record=None):
        return {
            'room_id': self._room_id,
            'from': 'dummy',
            'message': msg,
            'message_format': self._message_format,
            'notify': self._notify,
            }

    def send(self, *args, **kwds):
        req = self.build(*args, **kwds)
        self._send(req)
        return self._conn.method(
            self._api,
            self._method,
            req,
            timetout=self._timetout,
            )

    def close(self):
        pass
