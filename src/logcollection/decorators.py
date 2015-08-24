# -*- coding: utf-8 -*-
import logging
from .loggers import getLogger


def flush_error_log(message, name='root', level=logging.ERROR):
    def _wrap_func(func):
        def _wrap(*args, **kwds):
            logger = getLogger(name)
            try:
                rc = func(*args, **kwds)
                if rc:
                    logger.log(level, 'return code=%s: %s', rc, message)
            except Exception:
                logger.exception(message)
        return _wrap
    return _wrap_func
