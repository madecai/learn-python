from openpyxl import Workbook
import statistics as stats

book = Workbook()
sheet = book.active
rows = (
	['分数', '语文', '数学', '英语'],
	['张三', 70, 60, 50],
	('李四', 80, 90, 100),
	('王五', 90, 100, 90),
)
# 写入
for row in rows:
	sheet.append(row)

# 读取
values = []
for rows in sheet.iter_rows(min_row=2, min_col=2):
	for row in rows:
		row.value and values.append(row.value)
		print(row.value, end=" ")
	print()

print('长度', len(values))
print('最大值', max(values))
print('求和', sum(values))
print('平均值', stats.mean(values))
print('中值', stats.median(values))
print('标准差', stats.stdev(values))
print('总体方差', stats.variance(values))

