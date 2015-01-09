#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import logging
import logging.config
import argparse

import requests


class SlackHandler(logging.Handler):
    def __init__(self, url, channel, username, *args, **kwds):
        logging.Handler.__init__(self, *args, **kwds)
        self._url = url
        self._channel = channel
        self._username = username

    def emit(self, record):
        try:
            self._send_message(record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def _build_message(self, record):
        data = self.format(record)
        return json.dumps({
            'channel': self._channel,
            'username': self._username,
            'message': data,
        })

    def _send_message(self, record):
        msg = self._build_message(record)
        requests.post(self._url, msg)


class HipChatHandler(logging.Handler):
    def __init__(self, *args, **kwds):
        logging.Handler.__init__(self, *args, **kwds)

    def emit(self, record):
        try:
            msg = '{} :{}'.format(HOSTNAME, self.format(record))
            color = ''
            notify = False
            if record.levelname == "ERROR":
                notify = True
                color = 'red'
            send_message(message=msg, notify=notify, color=color, message_from="gunosy_redshift")
        except:
            pass


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf')
    args = parser.parse_args()

    logging.config.fileConfig(args.conf)

    logger = logging.getLogger('GHROEGHREO')
    logger.error('TEST')


if __name__ == '__main__':
    main()
