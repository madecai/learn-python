print('==========生成一个自然序列')
r = range(5)
print(r) # range(0, 5)
print(type(r)) # <class 'range'>
print('把range转成序列输出', list(r)) #[0, 1, 2, 3, 4]
print('==========range三个参数')
print('1、起始位置（可以省略，默认是0）')
print('2、终止位置')
print('3、步长')
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print('==========遍历range')   
for item in range(5) :
    print(item, end='、')
print()
