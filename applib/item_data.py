from selenium.webdriver.chrome.webdriver import WebDriver
from applib.extract.sku import Sku
from applib.extract.item import Item
from applib.extract.description import Description
from applib.extract.rrp import Rrp
from applib.extract.discount import Discount
from applib.extract.sale import Sale
from applib.extract.product_details import ProductDetails
from logging import Logger



class ItemData:
    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    def extract(self) -> tuple:
        """
        Return item data.
        """

        data = {
            'sku': Sku(driver=self._driver, logger=self._logger).extract(), 
            'item': Item(driver=self._driver, logger=self._logger).extract(), 
            'description': Description(driver=self._driver, logger=self._logger).extract(), 
        }

        product_details = ProductDetails(driver=self._driver, logger=self._logger).extract()

        data.update({
            'size': product_details['size'],
            'weight': product_details['weight'],
            'rrp': Rrp(driver=self._driver, logger=self._logger).extract(),
            'discount_price': Discount(driver=self._driver, logger=self._logger).extract(), 
            'promotion_price': Sale(driver=self._driver, logger=self._logger).extract(),
        })
 
        self._logger.info(data)
 
        return tuple(data.values())
