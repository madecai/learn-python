from openpyxl import Workbook
from openpyxl.styles import Alignment

wb = Workbook()
sheet = wb.active

sheet.freeze_panes = 'B2'

wb.save('test05_冻结窗格.xlsx')