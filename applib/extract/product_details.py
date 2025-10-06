from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from applib.extract.base_extractor import BaseExtractor



class ProductDetails(BaseExtractor):
    def extract(self) -> dict:
        """
        Return dict containing 'size' and 'weight' of item.
        """
        data = { 'size': '', 'weight': '', }

        button = self._details_button_element()
        if not button:
            return data
        
        button_initial_height = self._driver.execute_script('return arguments[0].clientHeight', button)

        self._click_on_element(button) # open

        details_specs = self._details_specs_elements()
        if len(details_specs) < 6:
            self._logger.debug('Not enough detail elements found, returning empty data.')
            self._click_on_element(button) # close          
            return data
        
        size = ' '.join([details_specs[i].text for i in range(3, 6)])
        weight = details_specs[1].text

        data.update({ 'size': size, 'weight': weight, })
        
        WebDriverWait(self._driver, 10).until(
            lambda d: d.execute_script('return arguments[0].clientHeight', button) > button_initial_height
        )

        self._click_on_element(button) # close

        current_height = self._driver.execute_script('return arguments[0].clientHeight', button)

        WebDriverWait(self._driver, 10).until(
            lambda d: d.execute_script('return arguments[0].clientHeight', button) == current_height
        )

        self._logger.info('size: %s', size)
        self._logger.info('weight: %s', weight)

        return data



    def _details_button_element(self) -> WebElement | None:
        """
        Return element to open Product Details. If could not found return None.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'div.product__block.product__block--product-details'),
            condition=EC.element_to_be_clickable,
            description='Details button',
        )


    def _details_specs_elements(self) -> list[WebElement]:
        """
        Return the list of elements with specs of Item. If could not found return an empty list.
        """
        selector=(By.CSS_SELECTOR, 'ul.product-details-list > li')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_all_elements_located(selector)
            )
        except TimeoutException:
            self._logger.info('could not found Details content elements. Return empty list.')
            return []


    def _details_element(self, parent) -> WebElement | None:
        try:
            return parent.find_element(By.TAG_NAME, 'details')
        except Exception:
            self._logger.info('Can not find details tag.')
            return None