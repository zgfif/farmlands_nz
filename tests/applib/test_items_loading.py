import unittest
from applib.items_loading import ItemsLoading
from applib.browser import Browser



class TestScrollItems(unittest.TestCase):
    def test_show_items(self):
        url = 'https://shop.farmlands.co.nz/collections/animal-type-calf'
        
        with Browser() as browser:    
            browser.open(url=url)

            if not browser.driver:
                return

            ItemsLoading(driver=browser.driver, logger=browser.logger).perform()
