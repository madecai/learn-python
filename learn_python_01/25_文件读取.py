print('==================================打开文件')
# open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
file_obj = open('./file_test/test_01.txt')
print(file_obj) # <_io.TextIOWrapper name='./file_test/test_01.txt' mode='r' encoding='cp936'>
print(type(file_obj)) # <class '_io.TextIOWrapper'>

print(r'window系统可以使用\替换/',r'需要转义，所有使用双\\', '或者前面加r代表不转义字符串')
file_obj = open('.\\file_test\\test_01.txt')
print(file_obj)
file_obj = open(r'.\file_test\test_01.txt')
print(file_obj)
print('通常使用/就行，会自动适配')
print('==================================读取文件')
file_obj = open('./file_test/test_01.txt')
content = file_obj.read() # 将所有文件内容作为字符串返回
print(content)
print('==================================关闭文件')
file_obj.close()
print('==================================with ... as 语句，这种写法会自动关闭')
with open('./file_test/test_01.txt') as file_obj:
    print(file_obj.read())
print('==================================配合try使用')
file_name = 'xxx'
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except:
    print(f'{file_name}文件不存在')
print('==================================文件中含有中文会报错')
# 读取中文不指定字符会报错，指定encoding，默认是None
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x8a in position 13: incomplete multibyte sequence
with open('./file_test/test_02.txt', encoding='utf-8') as file_obj:
        print(file_obj.read())
print('==================================读取大文件方式')
file_name = './file_test/test_02.txt'
try:
    with open(file_name, encoding='utf-8') as file_obj:
        file_content = ''
        chunk = 100
        while True:
            # read接受一个参数，默认值为-1
            # 每一次读取都是从上一次读取到的位置开始
            # 如果已经到最后则会返回''字符串
            content = file_obj.read(chunk)
            if not content:
                break
            file_content += content
        print(file_content)
except FileNotFoundError:
    print(f'{file_name}文件不存在')

print('==================================读取一行')
file_name = './file_test/test_03.txt'
with open(file_name, encoding='utf-8') as file_obj:
    print(file_obj.readline())
print('==================================一行一行的读')
import pprint
with open(file_name, encoding='utf-8') as file_obj:
    # 返回每行数据的列表
    content = file_obj.readlines()
    print(content) # ['aaa\n', '啊啊啊']
    # 使用pprint格式比较清晰
    pprint.pprint(content) 
print('==================================一行一行的读方式2')
with open(file_name, encoding='utf-8') as file_obj:
    for line_text in file_obj:
        print(line_text)