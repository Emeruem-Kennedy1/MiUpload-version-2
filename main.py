from sheet_class import *



if __name__ == '__main__':
    sh = Sheet('test_sheet')
    
    sh.edit_col('test_sheet_2' ,5,'e', ['Kennedy', 'boys', 'look at me', 100, 40, 'Man', 'woman', 50, '50 cent'])
    print(sh.get_sheet('test_sheet_2'))