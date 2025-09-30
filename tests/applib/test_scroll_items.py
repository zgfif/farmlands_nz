import unittest
from applib.scroll_items import ScrollItems
from applib.browser import Browser



class TestScrollItems(unittest.TestCase):
    def test_scroll_items(self):
        url = 'https://shop.farmlands.co.nz/collections/animal-type-calf'
        browser = Browser()
        browser.open(url=url)

        scrolling = ScrollItems(driver=browser.driver)
        
        scrolling.perform()

        browser.close()