#__author:"HYK"
#DATE:2018/4/5

# for i in range(3):
#     print(i)


_user = "alex"
_passwd = "abc123"


for i in range(3):
    username = input("username:")
    password = input("password:")

    if username == _user and password ==_passwd:
        print("Welcome %s login ..." %_user)
        passed_authentication = True
        break
    else:
        print("Invalid username or password!")
else: #只要上面的for循环正常执行完毕，中间没被打断，就会执行else语句
    print('要不要脸，臭流氓！')

# passed_authentication = False #标志位
#
#
# for i in range(3):
#     username = input("username:")
#     password = input("password:")
#
#     if username == _user and password ==_passwd:
#         print("Welcome %s login ..." %_user)
#         passed_authentication = True
#         break
#     else:
#         print("Invalid username or password!")
# if not  passed_authentication:
#     print('要不要脸，臭流氓！')