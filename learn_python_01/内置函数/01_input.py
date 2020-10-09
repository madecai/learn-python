print('ctrl + b不能使用input交互，使用sublimeRepl方式，配置快捷键f5')
# 获取用户输入的用户名
username = input('请输入你的用户名:')
# 判断用户名是否是admin
if username == 'admin' :
    print('欢迎管理员光临！')