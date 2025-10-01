from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from logging import Logger




class Discount:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def extract(self) -> str:
        """
        Return discount.
        """
        discount_table_element = self._discount_table_element()

        if not discount_table_element:
            return ''
        
        text = discount_table_element.text
        
        self._logger.info('discount: %s', text)
        
        return text
    


    def _discount_table_element(self) -> WebElement|None:
        """
        Return table discount element. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'table.shopacado-discount-table')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.info('could not found discount table element. Return None.')
