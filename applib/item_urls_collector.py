from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger




class ItemUrlsCollector:
    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def collect(self) -> list[str|None]:
        """
        Return list containing items urls.
        """
        items = self._items_elements()
        
        return [
            item.find_element(By.TAG_NAME, 'a').get_attribute('href') 
            for item in items
        ]



    def _items_elements(self) -> list[WebElement]:
        """
        Return list of item elements (div.f-column.card).
        If no elements are found, return an empty list.
        """
        selector = (By.CSS_SELECTOR, "div.f-column.card")
        
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located(selector)
            )
        except TimeoutException:
            self._logger.warning('No items found.')
            return []
