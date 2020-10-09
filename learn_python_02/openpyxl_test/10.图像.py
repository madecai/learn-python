from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
sheet = wb.active

# 报错：ImportError: You must install Pillow to fetch image objects
# 解决：安装Pillow， pip3 install Pillow
img = Image('app.png')
sheet['A1'] = 'xxx'

sheet.add_image(img, 'B2')

wb.save('test07_图像.xlsx')