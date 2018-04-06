#__author:"HYK"
#DATE:2018/4/6

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                '使馆区':{},
                'apple':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{},
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            '五道口':{
                '谷歌':{},
                '网易':{},
                'Soho':{},
                'Sogo':{},
                '快手':{},
            },
            '中关村':{
                'youku':{},
                'Iqiyi':{},
                '汽车之家':{},
                '新东方':{},
                'QQ':{},
            }
        },
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                '高盛':{},
                '摩根':{},
            },
            '外滩':{},
        },
        '闵行':{},
        '静安':{},
    },
    '山东':{
        '济南':{
        },
        '德州':{
            '乐陵':{
                '丁务镇':{},
            },
            '平原县':{},
        },
        '青岛':{},
    },
}

current_layer = menu  #实现动态循环
parent_laye = []     #保存所有父级，最后一个元素永远都是父亲级
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0: continue
    if choice in current_layer:
        print(current_layer)
        parent_laye.append(current_layer)
        print(parent_laye)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_laye:
            current_layer = parent_laye.pop()
    else:
        print("无此项")