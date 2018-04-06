#__author:"HYK"
#DATE:2018/4/5

exit_flag = False
for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("layer2",j)
        if j == 6:
            exit_flag = True  #儿子跳楼了
            break
    if exit_flag: #发现儿子跳楼，i jump
        break