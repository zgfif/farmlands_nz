from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from applib.extract.base_extractor import BaseExtractor



class Item(BaseExtractor):
    def extract(self) -> str:
        """
        Return name of item. Returns empty string if not found.
        """
        item_element = self._item_element()
        if not item_element:
            return ''
        
        text = item_element.text.strip()
        if not text:
            self._logger.debug('Item is found, but text is empty.')

        self._logger.info('item: %s', text)
        return text
    

    def _item_element(self) -> WebElement | None:
        """
        Return element containing name of item. If could not found return None.
        """
        return self._find_element(
            selector = (By.CSS_SELECTOR, 'h1.product__title.h3'),
            condition=EC.visibility_of_element_located,
            description='Item',
        )
