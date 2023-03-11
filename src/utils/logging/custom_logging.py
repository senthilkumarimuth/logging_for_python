"""
This module has factory design pattern for python logging
"""

import logging


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
       """ Virtually private constructor. """
       if Singleton.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          Singleton.__instance = self


class CustomLogging(Singleton):

    FORMATTER = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"

    def __init__(self):
        pass

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


class LoggingFactory():

    def __init__(self):
        pass

    def Factory(self):
        """Factory Method"""
        print("return same instance")
        return CustomLogging()

if __name__ == "__main__":
    logger = CustomLogging().app_logger('test', logging.DEBUG)
    logger.debug('app logging message')
    mod_log = CustomLogging().module_logger(__name__)
    mod_log.debug('modulue logging message')


