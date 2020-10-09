from openpyxl import Workbook
from openpyxl.chart import (
	Reference,
	Series,
	BarChart,
	PieChart,
	LineChart
)

wb = Workbook()
sheet = wb.active

rows = [
    ("USA", 46),
    ("China", 38),
    ("UK", 29),
    ("Russia", 22),
    ("South Korea", 13),
    ("Germany", 11)
]

for row in rows:
    sheet.append(row)

print('====================柱状图====================')
data = Reference(sheet, min_row=1, min_col=2, max_row=6)
categories = Reference(sheet, min_row=1, max_row=6, min_col=1)

chart = BarChart()
chart.title = '我是标题'
chart.add_data(data)
chart.set_categories(categories)

# 关闭图例和主要网格线
chart.legend = None
chart.y_axis.majorGridlines = None

# 每个条形都有不同颜色
chart.varyColors = True

sheet.add_chart(chart, 'A8')

print('====================饼状图====================')

pie = PieChart()
pie.title = "水果销售占比"

pie.add_data(data)
pie.set_categories(categories)

sheet.add_chart(pie, 'K8')

wb.save('test08_图表.xlsx')