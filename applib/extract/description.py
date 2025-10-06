from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from applib.extract.base_extractor import BaseExtractor
from time import sleep



class Description(BaseExtractor):
    def extract(self) -> str:
        """
        Return description of item. If not found, return empty string.
        """
        button = self._description_button_element()
        if not button:
            return ''
        
        button_initial_height = self._driver.execute_script('return arguments[0].clientHeight', button)

        # open description block
        self._click_on_element(button)        

        content = self._description_content_element()
        if not content:
            return ''
        
        # extract description content
        text = content.text.strip()
        if not text:
            self._logger.debug('Description content is empty.')
        
        WebDriverWait(self._driver, 10).until(
            lambda d: d.execute_script('return arguments[0].clientHeight;', button) > button_initial_height
        )

        # close description block
        self._click_on_element(button)
        
        WebDriverWait(self._driver, 10).until(
            lambda d: d.execute_script('return arguments[0].clientHeight;', button) == button_initial_height
        )

        self._logger.info('description: %s', text)
        return text



    def _description_button_element(self) -> WebElement | None:
        """
        Return element to open Description. If could not found, return None.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'div.product__block.product__block--collapsible_tab'),
            condition = EC.presence_of_element_located,
            description='description button',
        )



    def _description_content_element(self) -> WebElement | None:
        """
        Return element containing Description. If could not found return None.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'div.accordion-details__content.rte'),
            condition = EC.visibility_of_element_located,
            description='description content',
        )


    def _details_element(self) -> WebElement | None:
        """
        Details element.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'div.product__block.product__block--collapsible_tab > details > div'),
            condition = EC.visibility_of_element_located,
            description='details content',
        )
