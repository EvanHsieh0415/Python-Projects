import json

print('Command List | 指令列表')
print('setup - 還原meal.json並回到初始狀態')
print('add - 增加餐點')
print('backup - 備份meal.json到meal_backup.json')
print('return - 從meal_backup.json還原meal.json')
print('list - 顯示meal.json')
print('leave - 離開此程式')

sure_l = ['y', 'yes']

while True:
    command = input('Commands> ')

    if command == 'setup':
        sure = input('這將會清空meal.json，是否確定?(Y/N)> ')
        if sure.lower() in sure_l:
            data = {'count':0,'index':{}}
            with open('meal.json', mode='w', encoding='utf8') as file:
                json.dump(data, file, indent=4)
            print('已重新設定meal.json')
        else:
            print('已取消重新設定meal.json')
    elif command == 'add':
        while True:
            with open('meal.json', mode='r', encoding='utf8') as file:
                data = json.load(file)
            name = input('餐點名稱> ')
            price = int(input('餐點價格> '))
            count = 0
            member = []
            money = 0
            data['index'][name]= {'price':price, 'count':count, 'member':member, 'money': money}
            data['count'] = len(data['index'])
            with open('meal.json', mode='w', encoding='utf8') as file:
                json.dump(data, file, indent=4)
            print(f'{name}已新增 價格為{price}')
            while True:
                keep = input('繼續新增餐點?(Y/N) > ')
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
    elif command == 'backup':
        with open('meal.json', mode='r', encoding='utf8') as file:
            data = json.load(file)
        with open('meal_backup.json', mode='w', encoding='utf8') as backup:
            json.dump(data, backup, indent=4)
        print('已備份完成')
    elif command == 'return':
        with open('meal_backup.json', mode='r', encoding='utf8') as backup:
            data = json.load(backup)
        with open('meal.json', mode='w', encoding='utf8') as file:
            json.dump(data, file, indent=4)
        print('已從備份復原檔案')
    elif command == 'leave':
        break