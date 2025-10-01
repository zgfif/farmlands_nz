import unittest
from applib.item_data import ItemData
from applib.browser import Browser



class TestItemData(unittest.TestCase):
    def test_extract_item_data(self):
        url = 'https://shop.farmlands.co.nz/products/reliance-free-range-pellets-25kg'

        browser = Browser()
        
        browser.open(url=url)
        
        data = ItemData(driver=browser.driver).extract()
        
        self.assertIsInstance(data, dict)
        
        print(data)