from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from typing import Optional




class ItemsLoading:
    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def perform(self) -> None:
        """
        Perform click on button 'load more' while it exists.
        """
        self._logger.info('Loading items...')
        
        while True:           
            load_more_button = self._load_more_button_element()
            if not load_more_button:
                break
            
            try:
                self._click_on_element(load_more_button)
                self._logger.info("Click 'load more'...")
            except StaleElementReferenceException:
                self._logger.debug("'Load more' button went stale, retrying...")
                continue

        self._logger.info('Finish loading items.')



    def _click_on_element(self, element: WebElement) -> None:
        """
        Scroll element into visible area and click on it.
        """
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'instant', block: 'center', inline: 'end' });", 
            element
        )
        element.click()


    
    def _load_more_button_element(self) -> Optional[WebElement]:
        """
        Return Load more button element. If could not found return None.
        """
        selector = (By.CSS_SELECTOR, "button[type='load_more']")
        
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            self._logger.debug("'Load more' button not found. Return None.")
