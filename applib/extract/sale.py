from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from logging import Logger



class Sale:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def extract(self) -> str:
        """
        Return sale price of item.
        """
        sale_element = self._sale_element()

        if not sale_element:
            return ''
        
        text = sale_element.text

        self._logger.info('sale: %s', text)
        
        return text
    


    def _sale_element(self) -> WebElement|None:
        """
        Return element containing sale price. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'div.f-price-item.f-price-item--sale')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.info('could not found sale element. Return None.')
