print('==========三元运算符')
a = 30
b = 50
print('输出a和b较大的', a if a > b else b)
print('输出a和b较大的，并且b>100才输出', a if a > b else b if b > 100 else '')

print('==========条件判断')
if a < b : print(a)
print('==========条件判断执行多行，以空格或者Tab缩进，推荐空格')
# 设置subLime Tab转4个空格: "tab_size": 2,  "translate_tabs_to_spaces":  true
if a > b :
    print('a>b')
    print('a>b')
elif a == b :
    print('a==b')
    print('a==b')
else :
    print('b>a')
    print('b>a')


