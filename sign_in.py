import pygsheets as pg
import pandas as pd


class Sheet:
    def __init__(self, sheet_name: str):
        '''
        Initialize the google sheet
        params: sheet_name: str'''
        self.sheet_name = sheet_name
        self.c = pg.authorize(service_file='keys.json')
        self.sh = self.c.open(self.sheet_name)

    def create_sheet(self, sheet_title: str, rows: int, cols: int) -> None:
        '''
        Create a new sheet in the google sheet
        params: sheet_title: str, rows: int, cols: int
        '''
        self.sh.add_worksheet(sheet_title, rows=rows, cols=cols)


    def get_sheet(self, sheet_title: str) -> pd.DataFrame:
        '''
        Get the dataframe of a sheet
        params: sheet_title: str
        '''
        return pd.DataFrame(self.sh.worksheet_by_title(sheet_title).get_all_records())

    def get_worksheet_list(self) -> list:
        '''
        Get the list of worksheet names
        '''
        self.sh.worksheets()
        lists = []
        for sheet in self.sh.worksheets():
            lists.append(sheet.title)
        return lists


