from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

data = [
    ['Item', 'Colour'],
    ['pen', 'brown'],
    ['book', 'black'],
    ['plate', 'white'],
    ['chair', 'brown'],
    ['coin', 'gold'],
    ['bed', 'brown'],
    ['notebook', 'white'],
]

for r in data:
    sheet.append(r)

# 实际筛选的值不包括第一行
sheet.auto_filter.ref = 'A1:B8'
# B列默认选中这两个值
# 这会将相关指令添加到文件中，但不会实际过滤或排序
sheet.auto_filter.add_filter_column(1, ['brown', 'white'])
sheet.auto_filter.add_sort_condition('B2:B8')

wb.save('test02_过滤、排序.xlsx')