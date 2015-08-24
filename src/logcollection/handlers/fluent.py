# -*- coding: utf-8 -*-
import fluent.handler
import fluent.sendner


FluentHandler = fluent.handler.FluentHandler


class FluentSender(fluent.sender.FluentSender):
    def connect(self):
        self._reconnect()

    def build(self, msg, record=None):
        label = None
        timestamp = None
        return self._make_packet(label, timestamp, msg)

    def send(self, *args, **kwds):
        req = self.build(*args, **kwds)
        return self._send(req)

    def close(self):
        self._close()
