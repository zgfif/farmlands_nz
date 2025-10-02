import unittest
from applib.items_urls import ItemsUrls
from applib.browser import Browser



class TestItemsUrls(unittest.TestCase):
    def test_collect(self):
        url = 'https://shop.farmlands.co.nz/collections/animal-type-sheep-lamb'
        
        browser = Browser()
        
        browser.open(url=url)
        if not browser.driver:
            return
        
        items_urls = ItemsUrls(driver=browser.driver, logger=browser.logger).collect()

        self.assertIsInstance(items_urls, list)
        self.assertEqual(len(items_urls), 32)

        browser.close()
