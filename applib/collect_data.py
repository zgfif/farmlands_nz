from applib.browser import Browser
from applib.scroll_items import ScrollItems
from applib.item_data import ItemData
from applib.xlsx_file import XlsxFile



class CollectData:
    def __init__(self, url: str) -> None:
        self._url = url



    def perform(self) -> None:
        browser = Browser()
        browser.open(url=self._url)

        scrolling = ScrollItems(driver=browser.driver, logger=browser.logger)
        scrolling.perform()

        for url in scrolling.items_urls:
            browser.open(url)
            data = ItemData(driver=browser.driver, logger=browser.logger).extract()
            XlsxFile(logger=browser.logger, filepath='data.xlsx').add_row(data)

        browser.close()