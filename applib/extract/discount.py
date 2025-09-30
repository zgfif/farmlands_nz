from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement




class Discount:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> str:
        discount_table_element = self._discount_table_element()

        if not discount_table_element:
            return ''
        return discount_table_element.text
    


    def _discount_table_element(self) -> WebElement|None:
        selector = (By.CSS_SELECTOR, 'table.shopacado-discount-table')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found discount table element. Return None.')
