from logging import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import Callable
from time import sleep




class BaseExtractor:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger



    def _find_element(self, selector: tuple[str, str], condition: Callable, description: str) -> WebElement | None:
        """
        Find element by selector and condition. If could not found return None.
        """
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                condition(selector)
            )
        except TimeoutException:
            self._logger.info('Could not found %s element. Return None.', description)
            return None



    def _click_on_element(self, element: WebElement) -> None:
        """
        Scroll element into visible area and click on it.
        """
        self._scroll_to_element(element)
        element.click()


    
    def _scroll_to_element(self, element: WebElement) -> None:
        """
        Scroll to element.
        """
        self._driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'instant', block: 'bottom', inline: 'end' });", 
            element
        )
