from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from time import sleep



class Size:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> str:
        details_button_element = self._details_button_element()

        if not details_button_element:
            return ''   
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'end' });", 
            details_button_element
        )
        details_button_element.click()
        
        details_content_element = self._details_content_element()

        if not details_content_element:
            return ''
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'end' });", 
            details_content_element[0]
        )
        sleep(5)

        text = details_content_element[3].text + ' ' + details_content_element[4].text + ' ' + details_content_element[5].text
        
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'end' });", 
            details_button_element
        )
        details_button_element.click()
        sleep(5)
        return text


    def _details_button_element(self) -> WebElement|None:
        selector = (By.XPATH, '//h2[contains(text(), "Product Details")]')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found Details button element. Return None.')



    def _details_content_element(self) -> list[WebElement]|None:
        selector = (By.CSS_SELECTOR, 'ul.product-details-list > li')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_all_elements_located(selector)
            )
        except TimeoutException:
            print('could not found Details content element. Return None.')