from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from applib.extract.base_extractor import BaseExtractor




class Discount(BaseExtractor):
    def extract(self) -> str:
        """
        Return discount text. If table not found, return empty string.
        """
        discount_table_element = self._discount_table_element()
        if not discount_table_element:
            return ''
        
        text = discount_table_element.text.strip()
        if not text:
            self._logger.debug('Discount table found, but text is empty.')
        
        self._logger.info('Discount: %s', text)
        return text
    


    def _discount_table_element(self) -> WebElement | None:
        """
        Return table discount element. If could not found return None.
        """
        return self._find_element(
            selector=(By.CSS_SELECTOR, 'table.shopacado-discount-table'),
            condition=EC.visibility_of_element_located,
            description='Table Discount',
        )
