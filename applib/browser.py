from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from applib.custom_chrome_options import CustomChromeOptions




class Browser:
    def __init__(self) -> None:
        options = CustomChromeOptions().setup()
        self._driver = webdriver.Chrome(options=options)



    def open(self, url: str) -> None:
        """
        Open page by url.
        """
        try:
            self._driver.get(url=url)
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            sleep(10)
        except TimeoutException:
            print('Could not load body.')
        except WebDriverException:
            print('Could not open url.')



    @property
    def driver(self) -> WebDriver:
        """
        Return the instance of driver.
        """
        return self._driver



    def close(self) -> None:
        """
        Close browser.
        """
        if not self._driver:
            return

        print('Closing browser...')
        self._driver.quit()
