import unittest
from applib.scroll_items import ScrollItems
from applib.browser import Browser



class TestScrollItems(unittest.TestCase):
    def test_scroll_items(self):
        url = 'https://shop.farmlands.co.nz/collections/animal-type-calf'
        browser = Browser()
        browser.open(url=url)

        if not browser.driver:
            return

        scrolling = ScrollItems(driver=browser.driver, logger=browser.logger)
        
        scrolling.perform()

        browser.close()