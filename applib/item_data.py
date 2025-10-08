from selenium.webdriver.chrome.webdriver import WebDriver
from applib.extract.sku import Sku
from applib.extract.item import Item
from applib.extract.description import Description
from applib.extract.rrp import Rrp
from applib.extract.discount import Discount
from applib.extract.sale import Sale
from applib.extract.product_details import ProductDetails
from logging import Logger
from typing import Type
from applib.extract.base_extractor import BaseExtractor




class ItemData:
    EXTRACTORS = {
        'sku': Sku,
        'item': Item,
        'description': Description,
        'rrp': Rrp,
        'discount_price': Discount,
        'promotion_price': Sale,
    }


    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    def extract(self) -> tuple[str, ...]:
        """Return item data."""
        data = { key: self._extract(value, key) for key, value in self.EXTRACTORS.items() }

        data.update(**self._extract_product_details())

        self._logger.info('Extracted item data: %s .', data)

        missing = [k for k, v in data.items() if not v]
        if missing:
            self._logger.info('Some fields are empty: %s', missing)
 
        return tuple(data.get(key, '') for key in (
            'sku', 'item', 'description', 'size', 'weight','rrp', 'discount_price', 'promotion_price',
        ))


    def _extract(self, extractor_cls: Type['BaseExtractor'], field_name: str) -> str:
        """Extract value of attribute."""
        try:
            return extractor_cls(driver=self._driver, logger=self._logger).extract()
        except Exception as e:
            self._logger.warning('Failed to extract \'%s\': %s', field_name, e)
            return ''


    def _extract_product_details(self) -> dict[str, str]:
        """Extract size and weight details from product page."""
        try:
            return ProductDetails(driver=self._driver, logger=self._logger).extract()
        except Exception as e:
            self._logger.warning('Failed to extract Product Details %r', e)
            return { 'size': '', 'weight': '' }
