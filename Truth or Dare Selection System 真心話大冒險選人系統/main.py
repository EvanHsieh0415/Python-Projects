'''
Made By Mango
Discord: YT Mango#4092
Versoin : 1.0
'''
import random
import json

while True:

    list = []
    dict = {}

    while True:
        name = input('請輸入人名 (輸入-1結束輸入) > ')
        if name == '-1':
            break
        else:
            list.append(name)
    list_backup = list

    while True:
        for i in range(len(list)):
            dict[random.choice(list)] = random.choice(list)
        for i in dict:
            if i == dict[i]:
                list = list_backup
                break
        else:
            test = dict.values()
            for i in test:
                if list.count(i) >= 2:
                    break
            else:
                for i in range(len(list)):
                    if list[i] not in dict.values() or list[i] not in dict.keys():
                        break
                else:
                    break
    print(json.dumps(dict, indent=4, sort_keys=True))
    keep = ['y', 'yes']
    keep_ = input('還要再次選嗎? 請輸入y 或是yes > ')
    if keep_.lower() not in keep:
        break