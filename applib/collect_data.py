from applib.browser import Browser
from applib.scroll_items import ScrollItems
from applib.item_data import ItemData
from applib.xlsx_file import XlsxFile
import logging


class CollectData:
    def __init__(self, url: str) -> None:
        self._url = url
        self._logger = logging.getLogger('some')
        self._logger.setLevel(logging.DEBUG)

    
    def perform(self) -> None:
        browser = Browser()
        browser.open(url=self._url)


        scrolling = ScrollItems(driver=browser.driver)
        scrolling.perform()

        for url in scrolling.items_urls:
            browser.open(url)
            data = ItemData(driver=browser.driver).extract()
            XlsxFile(logger=self._logger, filepath='data.xlsx').add_row(data)

        browser.close()