from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger




class ItemUrlsCollector:
    TIMEOUT = 10
    ITEM_SELECTOR = (By.CSS_SELECTOR, "div.f-column.card")


    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    def collect(self) -> list[str]:
        """
        Collects and returns a list of item URLs from the page.
        Only items that contain a valid <a href="..."> are included.
        """
        return [
            href
            for item in self._items_elements()
            if (link := self._link_element(item)) 
            and (href := link.get_attribute('href'))
        ]


    def _items_elements(self) -> list[WebElement]:
        """
        Return list of item elements (div.f-column.card).
        If no elements are found, return an empty list.
        """
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_all_elements_located(self.ITEM_SELECTOR)
            )
        except TimeoutException:
            self._logger.warning('No items found.')
            return []


    def _link_element(self, parent_element: WebElement) -> WebElement | None:
        """Return link element. If could not found return None."""
        try:
            return parent_element.find_element(By.TAG_NAME, 'a')
        except NoSuchElementException:
            print('can not find link.')
            self._logger.warning("Link not found for item.")
            return None
