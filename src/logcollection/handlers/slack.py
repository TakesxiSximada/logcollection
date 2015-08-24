# -*- coding: utf-8 -*-
import slack_log_handler


SlackLogHandler = slack_log_handler.SlackLogHandler


class SlackIncomingWebHookSender(object):
    api_url = 'https://{}/services/hooks/incoming-webhook?token={}'

    def __init__(self, domain, token, channel, username, icon_emoji=':gohst'):
        self._url = self.api_url.format(domain, token)
        self._channel = channel
        self._username = username
        self._icon_emoji = icon_emoji

    def connect(self):
        pass

    def build(self, msg, record=None):
        return json.dumps({
            'channel': self._channel,
            'username': self._username,
            'icon_emoji': self._icon_emoji,
            'text': msg,
            })

    def send(self, *args, **kwds):
        req = self.build(*args, **kwds)
        return requests.post(self._url, req, verify=False)

    def close(self):
        pass


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

    def build(self, msg, record=None):
        return {
            'token': self._token,
            'channel': self._channel,
            'username': self._username,
            'icon_emoji': self._icon_emoji,
            'text': msg,
            }

    def send(self, *args, **kwds):
        req = self.build(*args, **kwds)
        return requests.post(self._url, params=req, verify=False)

    def close(self):
        pass
