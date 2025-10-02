import unittest
from applib.custom_chrome_options import CustomChromeOptions
from selenium.webdriver.chrome.options import Options
import logging


class TestCustomChromeOptions(unittest.TestCase):
    def test_options(self):
        
        options = CustomChromeOptions(logger=logging.getLogger(__name__)).setup()

        self.assertIsInstance(options, Options)
        self.assertEqual(len(options.arguments), 2)
        self.assertIn('--user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0', options.arguments)
        self.assertIn('--window-size=1920,1080', options.arguments)



    def test_options_when_headless(self):
        options = CustomChromeOptions(headless=True, logger = logging.getLogger(__name__)).setup()

        self.assertIsInstance(options, Options)
        self.assertEqual(len(options.arguments), 3)
        self.assertIn('--user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0', options.arguments)
        self.assertIn('--headless=new', options.arguments)
        self.assertIn('--window-size=1920,1080', options.arguments)
