import json

print('Command List | 指令列表')
print('order - 點餐')
print('list - 顯示餐點列表')
print('leave - 離開此程式')

while True:
    command = input('command> ')
    if command == 'order':
        with open('meal.json', mode='r', encoding='utf8') as file:
            data = json.load(file)
        print(json.dumps(data['index'], sort_keys=True, indent=4))
        while True:
            name = input('餐點名稱> ')
            mlcount = input('餐點數目> ')
            member = input('餐點負責人')

            money = data['index'][name]['price'] * int(mlcount)

            data['index'][name]['count'] = mlcount
            if member not in data['index'][name]['member']:
                data['index'][name]['member'].append(member)
            data['index'][name]['money'] += money

            print(f'您所點的餐點為{name}, 數量為{mlcount}, 金額共{money}元')
            with open('meal.json', mode='w', encoding='utf8') as file:
                json.dump(data, file, indent=4)
            while True:
                keep = input('再次點餐?(Y/N) > ')
                if keep.lower() == 'y' or keep.lower() == 'n':
                    break
                else:
                    print(f'請輸入Y or N, 您輸入的是{keep}')
            if keep.lower() == 'n':
                break
    elif command == 'list':
        with open('meal.json', mode='r', encoding='utf8') as file:
            data = json.load(file)
        print(json.dumps(data['index'], sort_keys=True, indent=4))
    elif command == 'leave':
        while True:
            keep = input('確定離開此程式?(Y/N) > ')
            if keep.lower() == 'y' or keep.lower() == 'n':
                break
            else:
                print(f'請輸入Y or N, 您輸入的是{keep}')
        if keep.lower() == 'y':
            break
    else:
        print(f'指令 {command} 不存在, 請重新輸入')