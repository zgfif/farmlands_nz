from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from logging import Logger




class Sku:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def extract(self) -> str:
        """
        Return sku of item.
        """
        sku_element = self._sku_element()
        
        if not sku_element:
            return ''
        
        sku_value = sku_element.text.split(' ')[-1]

        self._logger.info('sku: %s', sku_value)

        return sku_value
    


    def _sku_element(self) -> WebElement|None:
        """
        Return element containing sku. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'div.product-custom-sku')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.info('could not found sku element. Return None.')
