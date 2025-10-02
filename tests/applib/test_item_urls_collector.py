import unittest
from applib.item_urls_collector import ItemUrlsCollector
from applib.browser import Browser



class TestItemsUrlsCollector(unittest.TestCase):
    def test_collect(self):
        url = 'https://shop.farmlands.co.nz/collections/animal-type-sheep-lamb'
        
        browser = Browser()
        
        browser.open(url=url)
        if not browser.driver:
            return
        
        items_urls = ItemUrlsCollector(driver=browser.driver, logger=browser.logger).collect()

        self.assertIsInstance(items_urls, list)
        self.assertEqual(len(items_urls), 32)

        browser.close()
