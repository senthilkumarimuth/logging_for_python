"""
This module has factory design pattern for python log_utils
"""

import logging


FORMAT_STRING = "%(asctime)s | %(process)d | %(name)s | %(funcName)s:%(lineno)d | %(levelname)s | %(message)s"


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super(
            OneLineExceptionFormatter,
            self).formatException(exc_info)
        return repr(result)  # or format into one line however you want to

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '') + ' - log formatted by oneliner'
        return s


FORMATTER = OneLineExceptionFormatter(FORMAT_STRING)


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
        try:
            from settings.config import config
            name = config["project"]["name"]
            cls.app_name = name
            loglevel = config["environments"]["development"]['loglevel']
            cls.log_level = eval("logging." + loglevel.strip().upper())
        except ModuleNotFoundError:
            cls.log_level = logging.DEBUG
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


