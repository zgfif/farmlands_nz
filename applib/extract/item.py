from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement




class Item:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> str:
        item_element = self._item_element()

        if not item_element:
            return ''
        return item_element.text
    


    def _item_element(self) -> WebElement|None:
        selector = (By.CSS_SELECTOR, 'h1.product__title.h3')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found item element. Return None.')
