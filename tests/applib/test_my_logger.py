import unittest
import logging
from applib.my_logger import MyLogger
import os
from pathlib import Path




class TestMyLogger(unittest.TestCase):
    def test_my_logger(self):
        logpath = 'logs/testlog.log'
        
        ml = MyLogger(logpath=logpath).setup()

        self.assertIsInstance(ml, logging.Logger)

        ml.debug('some message')
