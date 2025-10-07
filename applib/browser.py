from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from applib.custom_chrome_options import CustomChromeOptions
from applib.my_logger import MyLogger
from logging import Logger
from applib.with_mixin import WithMixin




class Browser(WithMixin):
    def __init__(self) -> None:
        self._driver: webdriver.Chrome | None = None
        self._logger = MyLogger().setup()
        self.start()


    def start(self) -> None:
        """
        Start Chrome driver with custom options.        
        """
        if self._driver is None:
            options = CustomChromeOptions(logger=self._logger, headless=False).setup()
            self._driver = webdriver.Chrome(options=options)
            self.logger.info('Browser started.')



    def open(self, url: str) -> None:
        """
        Open page by url.
        """
        if not self._driver:
            self.logger.error('Driver is not initialized.')
            return
        
        try:
            self.logger.info('Opening \'%s\' ...', url)
            self._driver.get(url=url)
            
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            self.logger.info('Page loaded successfully.')
        except TimeoutException:
            self.logger.error('Could not load body for %s .', url)
        except WebDriverException as e:
            self.logger.exception('WebDriverException while opening url: %s', e)



    @property
    def driver(self) -> webdriver.Chrome | None:
        """
        Return the instance of driver.
        """
        return self._driver



    @property
    def logger(self) -> Logger:
        """
        Return the instance of logger.
        """
        return self._logger



    def close(self) -> None:
        """
        Close browser.
        """
        if self._driver is None:
            return

        try:
            self.logger.info('Closing browser...')
            self._driver.quit()
        except WebDriverException:
            self.logger.warning('Driver is already closed or not available.')
        finally:
            self._driver = None

