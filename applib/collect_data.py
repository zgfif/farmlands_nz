from applib.browser import Browser
from applib.items_loading import ItemsLoading
from applib.item_data import ItemData
from applib.xlsx_file import XlsxFile
from applib.item_urls_collector import ItemUrlsCollector



class CollectData:
    def __init__(self, url: str, filepath: str = 'data.xlsx') -> None:
        self._url = url
        self._filepath = filepath



    def perform(self) -> None:
        browser = Browser()

        browser.open(url=self._url)
        
        if not browser.driver:
            return
        
        ItemsLoading(driver=browser.driver, logger=browser.logger).perform()
        
        items_urls = ItemUrlsCollector(driver=browser.driver, logger=browser.logger).collect()

        if not items_urls:
            return

        browser.logger.info('Start processing product urls...')

        xlsx = XlsxFile(logger=browser.logger, filepath=self._filepath)

        for url in items_urls:
            if url:
                browser.open(url)

            data = ItemData(driver=browser.driver, logger=browser.logger).extract()

            xlsx.add_row(tuple(data.values()))
        
        xlsx.close()
        
        browser.close()
