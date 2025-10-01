from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from logging import Logger



class Rrp:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def extract(self) -> str:
        """
        Return Recommended Retail Price (RRP).
        """
        rrp_element = self._rrp_element()

        if not rrp_element:
            return ''
        
        text = rrp_element.text

        self._logger.info('RRP: %s', text)
        return text
    


    def _rrp_element(self) -> WebElement|None:
        """
        Return element containing RRP. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, 'div.f-price.f-price--large')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.info('could not found RRP element. Return None.')
