from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from applib.extract.base_extractor import BaseExtractor



class Sku(BaseExtractor):
    def extract(self) -> str:
        """
        Return the SKU of the item. Returns empty string if element not found or text is empty.
        """
        sku_element = self._sku_element()
        if not sku_element:
            return ''
        
        text = sku_element.text.strip()
        if not text:
            self._logger.debug('SKU element found, but text is empty.')
        
        if ':' in text:
            sku_value = text.split(':')[-1].strip()
        else:
            sku_value = text.split()[-1]

        self._logger.info('sku: %s', sku_value)
        return sku_value
    


    def _sku_element(self) -> WebElement | None:
        """
        Return element containing sku. If could not found return None.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'div.product-custom-sku'),
            condition=EC.visibility_of_element_located,
            description='Sku',
        )
