from pathlib import Path
import logging




class MyLogger:
    def __init__(self, logpath: str = 'logs/app.log', level=logging.DEBUG) -> None:
        self._logpath = logpath
        self._level = level
        self._prepare_path(logpath)



    def setup(self) -> logging.Logger:
        logger = logging.getLogger(__name__)

        logger.setLevel(self._level)

        console_handler = logging.StreamHandler()

        file_handler = logging.FileHandler(filename=self._logpath, mode='a', encoding='utf-8')

        for handler in console_handler, file_handler:
            handler.setLevel(self._level)

            handler.setFormatter(self._formatter())

            logger.addHandler(handler)

        return logger


    
    def _prepare_path(self, path: str) -> None:
        """
        Prepare path for logs.
        """
        Path(path).parent.mkdir(parents=True, exist_ok=True)



    def _formatter(self) -> logging.Formatter:
        return logging.Formatter(
            fmt='%(asctime)s - %(levelname)s - %(message)s', 
            style='%',
            )
