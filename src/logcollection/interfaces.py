#-*- coding: utf-8 -*-
from zope.interface import (
    Interface,
    Attribute,
    )


class ILogger(Interface):
    def log(self, *args, **kwds):
        pass

    def debug(self, *args, **kwds):
        pass

    def info(self, *args, **kwds):
        pass

    def warn(self, *args, **kwds):
        pass

    def error(self, *args, **kwds):
        pass

    def exception(self, *args, **kwds):
        pass
