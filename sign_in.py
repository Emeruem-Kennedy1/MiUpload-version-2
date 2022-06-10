import pygsheets as gc
import pandas as pd

c = gc.authorize(service_file='./keys.json')

df = pd.DataFrame(columns=['Name', 'Email', 'Password'])

sheet_name = 'test_sheet'
sheet_title = 'Sheet1'

sh = c.open(sheet_name)
wks = sh.worksheet_by_title(sheet_title)


wks.set_dataframe(df, (1, 1))