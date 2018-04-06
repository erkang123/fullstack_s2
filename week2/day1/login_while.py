#__author:"HYK"
#DATE:2018/4/5

# counter = 0
# while True:
#     if counter > 2**32:
#         break
#     counter +=1

_user = "alex"
_passwd = "abc123"

counter = 0
while counter <3:
    username = input("username:")
    password = input("password:")
    if username == _user and password ==_passwd:
        print("Welcome %s login ..." %_user)
        passed_authentication = True
        break
    else:
        print("Invalid username or password!")
        counter +=1
    if counter == 3:
        keep_going_choice = input("还想玩吗？[yes/no]")
        if keep_going_choice =="y":
            counter = 0
        else:
            exit("再见！")
else: #只要上面的for循环正常执行完毕，中间没被打断，就会执行else语句
    print('要不要脸，臭流氓！')