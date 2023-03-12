"""
This module has factory design pattern for python logging
"""

import logging


class Singleton(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance

class CustomLogging(Singleton):

    #FORMATTER = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
    FORMATTER = "%(asctime)s | %(process)d | %(name)s | %(funcName)s:%(lineno)d | %(levelname)s | %(message)s"


    @classmethod
    def app_logger(cls,app_name,log_level):
        """
                A private method that interacts with the python
                logging
        """
        # create logger
        cls.logger = logging.getLogger(app_name)
        cls.ch = logging.StreamHandler()
        cls.logger.setLevel(log_level)
        cls.ch.setLevel(log_level)
        # create formatter
        formatter = logging.Formatter(CustomLogging.FORMATTER)
        # add formatter to ch
        cls.ch.setFormatter(formatter)
        # add ch to logger
        cls.logger.addHandler(cls.ch)
        return cls.logger

    @classmethod
    def module_logger(cls,name):
        """
        A static method called by other modules to initialize logger in
        their own module
        """

        cls.ch_logger = cls.logger.getChild(name)
        return cls.ch_logger


if __name__ == "__main__":
    s = CustomLogging()
    logger = s.app_logger('test', logging.DEBUG)
    print(id(s))
    logger.debug('app logging message')
    s1 = CustomLogging()
    mod_log = s1.module_logger(__name__)
    print(id(s1))
    mod_log.debug('modulue logging message')


