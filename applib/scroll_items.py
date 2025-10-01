from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger




class ScrollItems:
    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger
        self._urls = []



    def perform(self) -> None:
        """
        Perform scrolling of page while the is button 'load more'.
        """
        self._logger.info('current count of elemnts: %d', len(self._items_elements()))

        while self._load_more_button_element():
            self._scroll_to_bottom()
            
            sleep(5)
            
            button = self._load_more_button_element()
            
            if button:
                self._driver.execute_script('arguments[0].scrollIntoView()', button)
                button.click()
            
            sleep(1)

            self._logger.info('current count of elemnts: %d', len(self._items_elements()))

        self._logger.info('Stop scrolling.')
        items = self._items_elements()
        
        self._urls = [item.find_element(By.TAG_NAME, 'a').get_attribute('href') for item in items]
        
        sleep(6)



    def _scroll_to_bottom(self) -> None:
        """
        Scrolling to bottom of page.
        """
        self._logger.info('scrolling to the bottom...') 
        self._driver.execute_script('window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });')


    
    def _load_more_button_element(self) -> WebElement|None:
        """
        Return Load more button element. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, "button[type='load_more']")
        
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.info('Could not found Load more button element. Return None')



    def _items_elements(self) -> list[WebElement]:
        """
        Return list of item elements (div.f-column.card).
        If no elements are found, return an empty list.
        """
        selector = (By.CSS_SELECTOR, "div.f-column.card")
        
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located(selector)
            )
        except TimeoutException:
            self._logger.exception('Could not find any item elements. Returning empty list.')
            return []


    @property
    def items_urls(self) -> list:
        """
        Return items urls.
        """
        return self._urls
