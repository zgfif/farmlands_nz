from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from time import sleep




class ProductDetails:
    TIMEOUOT = 10

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver



    def extract(self) -> dict:
        """
        Extract data contains 'size' and 'weight'.
        """
        data = {
            'size': '',
            'weight': '',
        }

        details_button = self._details_button_element()

        if not details_button:
            return data
        
        self._click_on_element(details_button)
        details_specs = self._details_specs_elements()

        if not details_specs:
            return data
        
        data.update({
            'size': f'{details_specs[3].text} {details_specs[4].text} {details_specs[5].text}',
            'weight': details_specs[1].text,
        })

        self._click_on_element(details_button)

        return data




    def _details_button_element(self) -> WebElement|None:
        selector = (By.XPATH, '//h2[contains(text(), "Product Details")]')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('could not found Details button element. Return None.')



    def _details_specs_elements(self) -> list[WebElement]|None:
        selector = (By.CSS_SELECTOR, 'ul.product-details-list > li')

        try:
            return WebDriverWait(self._driver, self.TIMEOUOT).until(
                EC.visibility_of_all_elements_located(selector)
            )
        except TimeoutException:
            print('could not found Details content element. Return None.')



    
    def _click_on_element(self, element: WebElement) -> None:
        """
        Scroll element into visible area.
        """
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'bottom', inline: 'end' });", 
            element
        )
        sleep(1)
        element.click()
