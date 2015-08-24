# -*- coding: utf-8 -*-
import logging
from functools import lru_cache
from lazr.delegates import delegate_to
from .interfaces import ILogger


@delegate_to(ILogger, context='_context')
class LazyLogger(object):
    def __init__(self, name):
        self._name = name

    @property
    @lru_cache()
    def _context(self):
        return logging.getLogger(self._name)


def getLogger(*args, **kwds):
    return LazyLogger(*args, **kwds)
