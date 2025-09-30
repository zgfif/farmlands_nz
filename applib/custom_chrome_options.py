from selenium.webdriver.chrome.options import Options



class CustomChromeOptions:
    def __init__(self,) -> None:
        self._options = Options()
    

    def setup(self,) -> Options:
        """
        Configure options object for Chrome and return it.
        """
        # self._options.add_argument('--headless=new')
        self._options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0')
        self._options.add_argument('--window-size=1920,1080') 
        return self._options
