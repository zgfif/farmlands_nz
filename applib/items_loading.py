from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger




class ItemsLoading:
    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def perform(self) -> None:
        """
        Perform scrolling of page while the is button 'load more'.
        """
        self._logger.info('Loading items...')

        while self._load_more_button_element():
            sleep(1)
            load_more_button = self._load_more_button_element()
            
            if not load_more_button:
                break
            
            self._logger.info('Click \'load more\'...')
            self._click_on_element(load_more_button)
        
        self._logger.info('Stop loading items.')




    def _click_on_element(self, element: WebElement) -> None:
        """
        Scroll element into visible area and click on it.
        """
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'auto', block: 'bottom', inline: 'end' });", 
            element
        )
        sleep(1)
        element.click()


    
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
            self._logger.info('Could not found Load more button element. Return None.')
