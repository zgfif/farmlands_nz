from applib.browser import Browser
from applib.items_loading import ItemsLoading
from applib.item_data import ItemData
from applib.xlsx_file import XlsxFile
from applib.item_urls_collector import ItemUrlsCollector




class CollectData:
    def __init__(self, url: str, filepath: str = 'data.xlsx') -> None:
        self._url = url
        self._filepath = filepath



    def perform(self) -> bool:
        """Extract and save data to file."""
        with Browser() as browser:
            browser.open(url=self._url)

            if not browser.driver:
                browser.logger.warning('Driver not initialized for url: %s', self._url)
                return False

            # load all items on page
            ItemsLoading(driver=browser.driver, logger=browser.logger).perform()
            
            # collect items urls
            items_urls = ItemUrlsCollector(driver=browser.driver, logger=browser.logger).collect()

            browser.logger.info('Collected %d item URLs', len(items_urls))

            browser.logger.info('Start processing product urls...')

            with XlsxFile(logger=browser.logger, filepath=self._filepath) as file:
                self._process_urls(browser=browser, file=file, urls=items_urls)

            return True


    def _process_urls(self, browser: Browser, file: XlsxFile, urls: list[str]) -> None:
        """Extracts product data from given URLs and saves them into an Excel file."""
        for i, url in enumerate(urls, 1):
            try:
                browser.logger.info('[%d/%d] Processing %s', i, len(urls), url)
                browser.open(url)
                if not browser.driver:
                    return
                data = ItemData(driver=browser.driver, logger=browser.logger).extract()
                file.add_row(data)
            except Exception as e:
                browser.logger.error('Error during processing %s %s', url, e, exc_info=True)
