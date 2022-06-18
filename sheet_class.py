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

    def create_sheet(self, sheet_title: str, rows=200, cols=200) -> None:
        '''
        Create a new sheet in the google sheet
        params: sheet_title: str, rows: int, cols: int
        '''
        try:
            if sheet_title in self.get_worksheet_list():
                print('Sheet already exists')
                return
            self.sh.add_worksheet(sheet_title, rows, cols)
        except Exception as e:
            print(e)

    def set_header(self, sheet_title: str, header: list) -> None:
        '''
        Set the header of a sheet
        params: sheet_title: str, header: list
        '''
        try:
            if sheet_title not in self.get_worksheet_list():
                print('Sheet does not exist')
                return
            else:
                sheet_row_length = self.sh.worksheet_by_title(sheet_title).rows
                if len(header) > sheet_row_length:
                    print('Header is too long, please reduce the length or try adding new columns to the sheet')
                    return
                else:
                    self.sh.worksheet_by_title(sheet_title).update_row(1, header)
        except Exception as e:
            print(e)

    def get_sheet(self, sheet_title: str) -> pd.DataFrame:
        '''
        Get the dataframe of a sheet
        params: sheet_title: str
        '''
        try:
            return pd.DataFrame(self.sh.worksheet_by_title(sheet_title).get_as_df())
        except Exception as e:
            print(e)

    def get_worksheet_title_list(self) -> list:
        '''
        Get the list of worksheet names
        '''
        worksheets = self.sh.worksheets()
        worksheet_titles = [sheet.title for sheet in worksheets]
        return worksheet_titles
    
    def edit_row(self, sheet_title: str, row: int, values: list) -> None:
        '''
        Edit a whole row in the sheet
        params: sheet_title: str, row: int, values: list
        '''
        try:
            if sheet_title not in self.get_worksheet_title_list():
                print('Sheet does not exist')
                return
            else:
                if len(values) > self.sh.worksheet_by_title(sheet_title).rows:
                    print('Values is too long, please reduce the length or try adding new columns to the sheet')
                    return
                else:
                    self.sh.worksheet_by_title(sheet_title).update_row(row, values)
        except Exception as e:
            print(e)

    def edit_column(self, sheet_title: str, col: int,header, values: list) -> None:
        '''
        Edit a whole column in the sheet
        params: sheet_title: str, col: int, values: list
        '''
        try:
            if sheet_title not in self.get_worksheet_title_list():
                print('Sheet does not exist')
                return
            else:
                if len(values) + 1 > self.sh.worksheet_by_title(sheet_title).cols:
                    print('Values is too long, please reduce the length or try adding new columns to the sheet')
                    return
                else:
                    new_colum_values = [header, *values]
                    print(new_colum_values)
                    self.sh.worksheet_by_title(sheet_title).update_col(col, new_colum_values)
        except Exception as e:
            print(e)

    