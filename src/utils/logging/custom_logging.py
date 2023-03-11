"""
This module has factory design pattern for python logging
"""

import logging
from singleton import Singleton


class LoggerFactory(Singleton):

    FORMATTER = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"

    def __init__(self):
        self.logger = None
        self.ch_logger = None

    def app_logger(self,app_name,log_level):
        """
                A private method that interacts with the python
                logging
        """
        # create logger
        self.logger = logging.getLogger(app_name)
        ch = logging.StreamHandler()
        if log_level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
            self.ch.setLevel(logging.DEBUG)
        if log_level == "INFO":
            self.logger.setLevel(logging.INFO)
            self.setLevel(logging.INFO)
        # create formatter
        formatter = logging.Formatter(LoggerFactory.FORMATTER)
        # add formatter to ch
        self.ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(self.ch)
        return self.logger

    def module_logger(self,name):
        """
        A static method called by other modules to initialize logger in
        their own module
        """

        self.ch_logger = self.logger.getChild(name)
        return self.ch_logger

