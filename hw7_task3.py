# Task 3
from openpyxl import load_workbook
import time


class File:

    def __init__(self, file_name):
        self.file_obj = load_workbook(file_name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file_obj.close()


with File('homework_task3_1.xlsx') as file:
    sheet = file.active
    sheet['C1'] = 'Cursor'
    sheet['D1'] = 'Forever'
    now = time.strftime('%x ')
    now1 = time.strftime('%X')
    sheet['A1'] = now
    sheet['B1'] = now1
    file.save("homework_task3.xlsx")



