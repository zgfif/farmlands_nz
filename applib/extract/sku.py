from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement




class Sku:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> str:
        sku_element = self._sku_element()
        if not sku_element:
            return ''
        sku_value = sku_element.text.split(' ')[-1]
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
            print('could not found sku element. Return None.')
