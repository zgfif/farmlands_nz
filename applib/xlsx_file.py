from openpyxl import Workbook
import openpyxl
from pathlib import Path
from logging import Logger




class XlsxFile:
    COLUMNS = (
        'sku', 
        'item',
        'description', 
        'size', 
        'weight', 
        'rrp', 
        'discount_price', 
        'promotion_price',
    )

    def __init__(self, logger: Logger, filepath: str) -> None:
        self._filepath = filepath
        self._logger = logger
        self._prepare_file()
        self._workbook = openpyxl.load_workbook(self._filepath)
        
        self._sheet = self._workbook.active

    

    def add_row(self, data: tuple) -> None:
        """
        Add row to end of xlsx file.
        """
        if not self._sheet:
            self._logger.warning('No active sheet to add row.')
            return

        self._sheet.append(data)
        
        self._workbook.save(self._filepath)



    def rows(self) -> tuple:
        """
        Return rows from xlsx file.
        """
        if not self._sheet:
            self._logger.warning('no active sheet. Return an empty tuple.')
            return tuple()
        
        return tuple(row for row in self._sheet.iter_rows(min_row=1, max_row=self._sheet.max_row, values_only=True))



    def _prepare_file(self) -> None:
        """
        Prepare path for file.
        """
        file_path = Path(self._filepath)

        if Path.exists(file_path):
            self._logger.info('file %s already exists.', self._filepath)
            return
        
        self._logger.info('Create file %s ...', self._filepath)
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        self._create_with_columns()



    def _create_with_columns(self) -> None:
        """
        Create a xlsx file.
        """
        workbook = Workbook()
        
        sheet = workbook.active
        
        if not sheet:
            self._logger.warning('Could not found active sheet.')
            return

        sheet.append(self.COLUMNS)
        
        workbook.save(self._filepath)



    def close(self) -> None:
        """
        Close workbook.
        """
        if self._workbook:
            self._logger.debug('Closing %s ...', self._filepath)
            self._workbook.close()



    def __enter__(self):
        """
        Enter in with statement.
        """
        return self



    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit from with statement.
        """
        self.close()
