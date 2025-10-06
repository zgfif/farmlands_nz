import unittest
from applib.item_data import ItemData
from applib.browser import Browser



class TestItemData(unittest.TestCase):
    def test_extract_item_data(self):
        url = 'https://shop.farmlands.co.nz/products/reliance-free-range-pellets-25kg'

        with Browser() as browser:
            browser.open(url=url)

            if not browser.driver:
                return
            
            data = ItemData(driver=browser.driver, logger=browser.logger).extract()
            
            self.assertIsInstance(data, tuple)
            
            print(data)
