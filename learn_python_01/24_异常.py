print('======================1、捕获所有异常')
try:
    10 / 0
except:
    print('出错了')
else:
    print('程序正常执行')

print('=====================2、捕获指定异常')
arr = []
try:
    # print(c)
    # 10 / 0
    # arr[0]
    arr + 'hello'
except NameError:
    print('出现 NameError 异常')
except ZeroDivisionError:
    print('出现 ZeroDivisionError 异常')
except IndexError:
    print('出现 IndexError 异常')
except Exception as e :
    print('未知异常', e, type(e)) # can only concatenate list (not "str") to list <class 'TypeError'>
finally:
    print('无论如何都要执行')

print('=====================3、自定义异常，继承Exception')
class MyError(Exception):
    pass

def getUserById(id):
    if(id <= 0):
        raise MyError('用户id非法')
    return {'name': 'zhangsan'}

getUserById(1)