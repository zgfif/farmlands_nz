
from selenium.webdriver.chrome.webdriver import WebDriver
from applib.extract.sku import Sku
from applib.extract.item import Item
from applib.extract.description import Description
from applib.extract.size import Size
from applib.extract.weight import Weight
from applib.extract.rrp import Rrp
from applib.extract.discount import Discount
from applib.extract.sale import Sale
from applib.extract.product_details import ProductDetails



class ItemData:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver


    def extract(self) -> dict:
        """
        Return item data.
        """

        data = {
            'sku': Sku(driver=self._driver).extract(), 
            'item': Item(driver=self._driver).extract(), 
            'description': Description(driver=self._driver).extract(), 
        }

        product_details = ProductDetails(driver=self._driver).extract()

        data.update({
            'size': product_details['size'],
            'weight': product_details['weight'],
            'rrp': Rrp(driver=self._driver).extract(), 
            'discount_price': Discount(driver=self._driver).extract(), 
            'promotion_price': Sale(driver=self._driver).extract(),
        })

        return data
