from selenium.webdriver.chrome.options import Options
from logging import Logger




class CustomChromeOptions:
    def __init__(self,  logger: Logger, headless: bool = False, user_agent: str = '', window_size: str = '1920,1080') -> None:
        self._logger = logger
        self._headless = headless
        self._user_agent = user_agent or self._default_user_agent()
        self._window_size = window_size

        self._options = Options()



    def setup(self) -> Options:
        """Configure options object for Chrome and return it."""
        if self._headless:
            try:
                self._options.add_argument('--headless=new')
            except Exception:
                self._options.add_argument('--headless')
        
        if self._user_agent:
            self._options.add_argument(f'--user-agent={self._user_agent}')
        
        self._options.add_argument(f'--window-size={self._window_size}') 
        
        self._logger.info('Chrome options: %s .', self._options.arguments)
        return self._options



    def _default_user_agent(self) -> str:
        """Return default user-agent."""
        return 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0'
