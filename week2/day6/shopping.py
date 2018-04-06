#__author:"HYK"
#DATE:2018/4/5

# salary = 5000
# while True:
#     msg = '''
#             1.ipthon6s 5800
#             2.mac book 9000
#             3.coffee 32
#             4.python book 80
#             5.bicyle    1500
#     '''
#     print(msg)
#     print('您的当前余额是',salary)
#     you_choocie = input("请选择》：")
#     if you_choocie.isdigit():
#         you_choocie = int(you_choocie)
#         if you_choocie == 1:
#             print("余额不足",salary)
#         else:
#             exit("再见")
#     elif you_choocie == "quit":
#         exit('see you later!')
#     else:
#         print("输入有误！")


product_list = [
    ('Mac',9000),
    ('Kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('Bike',2000)
]

saving = input('please input your money:')
shopping_car = []

if saving.isdigit():
    saving = int(saving)
    while True:
        # for i in product_list:
        #     print(product_list.index(i),i)
        for v,i in enumerate(product_list,1):
            print(i,'>>',v)
        choice = input('选择购买商品编号【退出quit】：')
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice<=len(product_list):
               p_item =  product_list[choice-1]
               if p_item[1]<saving:
                   saving-=p_item[1]
                   shopping_car.append(p_item)
               else:
                   print('余额不足，还剩%s'%saving)
            else:
                print('输入的编码不存在')
        elif choice == 'q':
            print('您已购买的商品：')
            for i in shopping_car:
                print(i)
            print('您的余额是：%s'%saving)
            break
        else:
            print('输入有误！')
else:
    print('input error!')
