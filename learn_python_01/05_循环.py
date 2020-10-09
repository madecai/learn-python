# 引入time模块，使用time()函数获取当前时间，单位秒
from time import *
i = 0
while i < 5 : 
    j = 0
    while j < i + 1 : 
        print('* ', end='')
        j += 1
    print()
    i += 1
else : 
    print('退出循环', i)

print('==========输出乘法表')
begin = time()
i = 0
while i < 9 : 
    i += 1
    j = 0
    while j < i :
        j += 1
        print(f'{j}*{i}={i * j} ', end='')
    print()
end = time()
print(end - begin)
print('==========pass占位，没什么用')
if 1 < 2 : pass

i = 0
while i < 5 : 
    i += 1
    pass
