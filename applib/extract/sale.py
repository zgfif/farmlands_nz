from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from applib.extract.base_extractor import BaseExtractor



class Sale(BaseExtractor):
    def extract(self) -> str:
        """
        Return sale price of the item. Returns empty string if not found.
        """
        return ''
        sale_element = self._sale_element()

        if not sale_element:
            return ''
        
        text = sale_element.text.strip()
        if not text:
            self._logger.debug('Sale element found, but text is empty.')

        self._logger.info('Sale: %s', text)
        return text


    def _sale_element(self) -> WebElement | None:
        """
        Return element containing sale price. If could not found return None.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'div.f-price-item.f-price-item--sale'),
            condition=EC.visibility_of_element_located,
            description='Sale',
        )
