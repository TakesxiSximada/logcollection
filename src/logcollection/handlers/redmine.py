# -*- coding: utf-8 -*-
import redmine


class RedmineSender(object):
    def __init__(self, url, username, password, project_id=None,
                 tracker_id=None, status_id=None, assigned_to_id=None):
        self._url = url
        self._username = username
        self._password = password
        self._project_id = project_id
        self._tracker_id = tracker_id
        self._status_id = status_id
        self._assgined_to_id = assigned_to_id
        self._conn = None

    def connect(self):
        if not self._conn:
            self._conn = redmine.Redmine(
                self._url,
                self._username,
                self._password,
                )

    def build(self, msg, record=None):
        issue = self._conn.issue.new()
        issue.proejct_id = self._project_id
        issue.tracker_id = self._tracker_id
        issue.status_id = self._status_id
        issue.assigned_to_id = self._assigned_to_id

        issue.subject = u'error'
        issue.description = '''
        <pre>
          {}
        </pre>'''.format(msg)
        return issue

    def send(self, *args, **kwds):
        req = self.build(*args, **kwds)
        return req.save()
