from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from time import sleep



class Description:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> str:
        description_button_element = self._description_button_element()


        if not description_button_element:
            return ''   

        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'end' });", 
            description_button_element
        )
        description_button_element.click()
        
        description_content_element = self._description_content_element()

        if not description_content_element:
            return ''
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'end' });", 
            description_content_element
        )
        sleep(5)
        text = description_content_element.text
        
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'end' });", 
            description_button_element
        )

        description_button_element.click()
        sleep(5)
        return text




    def _description_button_element(self) -> WebElement|None:
        selector = (By.XPATH, '//h2[contains(text(), "Description")]')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found description element. Return None.')



    def _description_content_element(self) -> WebElement|None:
        selector = (By.CSS_SELECTOR, 'div.accordion-details__content.rte')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found description content element. Return None.')