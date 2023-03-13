"""
This module has factory design pattern for python log_utils
"""

import logging
import os
try:
    from log_formatter import FORMATTER
except ImportError:
    from .log_formatter import FORMATTER


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class CustomLogging(Singleton):
    logger = None

    @classmethod
    def set_appname_loglevel(cls):
        cls.logger = None
        if "APP_LOG_LEVEL" in os.environ:
            cls.log_level = os.getenv("APP_LOG_LEVEL")
            cls.log_level = eval("logging." + cls.log_level.strip().upper())
        else:
            cls.log_level = logging.DEBUG
        if "AppName" in os.environ:
            cls.app_name = os.getenv("AppName")
        else:
            cls.app_name = "AppLogger"

    @classmethod
    def app_logger(cls):
        """
                A private method that interacts with the python
                log_utils
        """
        # create logger
        if cls.logger is None:
            cls.set_appname_loglevel()
            cls.logger = logging.getLogger(cls.app_name)
            cls.logger.setLevel(cls.log_level)
            cls.ch = logging.StreamHandler()
            cls.ch.setLevel(cls.log_level)
            cls.ch.setFormatter(FORMATTER)
            cls.logger.addHandler(cls.ch)
        return cls.logger

    @classmethod
    def module_logger(cls, name):
        """
        A static method called by other modules to initialize logger in
        their own module
        """

        cls.ch_logger = cls.app_logger().getChild(name)
        return cls.ch_logger


if __name__ == "__main__":
    s = CustomLogging()
    logger = s.app_logger()
    print(id(s))
    logger.debug('app log_utils message')
    s1 = CustomLogging()
    mod_log = s1.module_logger(__name__)
    print(id(s1))
    mod_log.debug('modulue log_utils message')


