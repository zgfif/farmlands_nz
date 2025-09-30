from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement




class Rrp:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> str:
        rrp_element = self._rrp_element()

        if not rrp_element:
            return ''
        return rrp_element.text
    


    def _rrp_element(self) -> WebElement|None:
        selector = (By.CSS_SELECTOR, 'div.f-price.f-price--large')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found RRP element. Return None.')
