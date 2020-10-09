from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
sheet = wb.active

rows = (
    (34, 26),
    (88, 36),
    (24, 29),
)

total = 0
for row in rows:
	sheet.append(row)
	total = total + sum(row)

print('总数：', total)

cell = sheet.cell(row=4, column=2)
cell.value = '=sum(A1:B3)'
# 设置粗体
cell.font = Font(bold=True)

wb.save('test06_公式.xlsx')