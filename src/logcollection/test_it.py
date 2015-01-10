# -*- coding: utf-8 -*-
from unittest import TestCase


class LogCollectionTestCase(TestCase):
    def _target(self, *args, **kwds):
        return

    def _call(self, *args, **kwds):
        target = self._target()
        res = target.fuc(*args, **kwds)
        return res


class SlackIncommingWebHookSenderTest(LogCollectionTestCase):
    def _setting(self):
        from pit import Pit
        setting = {
            'domain': '.slack.com',
            'token': '',
            'channel': '#general',
            'username': '',
            'icon_emoji': ':ghost:',
            }
        return Pit.get(
            'logcollection-test-slack',
            {'require': setting},
            )

    def _target(self):
        from . import SlackIncomingWebHookSender
        setting = self._setting()
        return SlackIncomingWebHookSender(**setting)

    def _call(self, *args, **kwds):
        target = self._target()
        return target.send(*args, **kwds)

    def test_send(self):
        self._call('test message')
