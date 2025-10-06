import unittest
from applib.browser import Browser



class TestBrowser(unittest.TestCase):
    def test_opening_url(self):
        url = 'https://shop.farmlands.co.nz/collections/animal-type-calf'
 
        with Browser() as browser:
            browser.open(url=url)
            
            if not browser.driver:
                return
            
            self.assertEqual(browser.driver.current_url, url)
