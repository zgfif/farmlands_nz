from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from applib.custom_chrome_options import CustomChromeOptions
from applib.my_logger import MyLogger
import logging



class Browser:
    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=CustomChromeOptions().setup())
        self._logger = MyLogger().setup()



    def open(self, url: str) -> None:
        """
        Open page by url.
        """
        try:
            self.logger.info('Opening \'%s\' ...', url)

            self._driver.get(url=url)
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            sleep(5)
        except TimeoutException:
            self.logger.exception('Could not load body.')
        except WebDriverException:
            self.logger.exception('Could not open url.')



    @property
    def driver(self) -> WebDriver:
        """
        Return the instance of driver.
        """
        return self._driver



    @property
    def logger(self) -> logging.Logger:
        """
        Return the instance of logger.
        """
        return self._logger



    def close(self) -> None:
        """
        Close browser.
        """
        if not self._driver:
            return

        self.logger.info('Closing browser...')
        self._driver.quit()
