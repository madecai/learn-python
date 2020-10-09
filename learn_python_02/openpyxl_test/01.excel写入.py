from openpyxl import Workbook
import time

book = Workbook()
# 获取活动的sheet
sheet = book.active
# 赋值方式一
sheet['A1'] = 'aaa'
# 赋值方式二
sheet.cell(row=2, column=1).value = 'abc'

now = time.strftime("%x")
print(now)
sheet['A3'] = now

rows = (
	(1, 'a', 'b'),
	(2, 3, 4),
	('ab', 'ba', 'ac')
)

# 添加到末尾
for row in rows:
	sheet.append(row)

book.save("test01.xlsx")
