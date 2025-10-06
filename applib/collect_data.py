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
        with Browser() as browser:
            browser.open(url=self._url)

            if not browser.driver:
                return

            # load all items on page
            ItemsLoading(driver=browser.driver, logger=browser.logger).perform()
            
            # collect items urls
            items_urls = ItemUrlsCollector(driver=browser.driver, logger=browser.logger).collect()

            browser.logger.info('Start processing product urls...')

            with XlsxFile(logger=browser.logger, filepath=self._filepath) as file:
                for i, url in enumerate(items_urls, 1):
                    try:
                        browser.logger.info('[%d/%d] Processing %s', i, len(items_urls), url)
                        browser.open(url)
                        data = ItemData(driver=browser.driver, logger=browser.logger).extract()
                        file.add_row(data)
                    except Exception as e:
                        browser.logger.error('Error during processing %s %s', url, e)
