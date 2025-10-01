from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from logging import Logger



class Item:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def extract(self) -> str:
        """
        Return name of item.
        """
        item_element = self._item_element()

        if not item_element:
            return ''
        
        text = item_element.text

        self._logger.info('item: %s', text)
        return text
    


    def _item_element(self) -> WebElement|None:
        """
        Return element containing name of item. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'h1.product__title.h3')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.info('could not found item element. Return None.')
