import json
import csv

while True:
    while True:
        file_1 = input('File 1 Name > ')
        file_2 = input('File 2 Name > ')
        if isinstance(file_1, str) == True and isinstance(file_2, str) == True:
            break
        else:
            print('File name enter error')
    try:
        with open('en_us.json', mode='r', encoding='utf8') as enFile:
            enData = json.load(enFile)
        with open('zh_tw.json', mode='r', encoding='utf8') as zhFile:
            zhData = json.load(zhFile)
    except:
        print('Could not find files')
    else:
        break

data = {}
for i in zhData:
    data[zhData[i]] = enData[i]
    print(f'Replace {i}, schedule: {len(data)/len(file_1)}%')

while True:
    json_name = input('Json File Name > ')
    csv_name = input('CSV File Name > ')
    if isinstance(json_name, str) == True and isinstance(csv_name, str) == True:
        break
    else:
        print('File name enter error')

with open('ok.json', mode='w', encoding='utf8') as okFile:
    json.dump(data, okFile, sort_keys=True, indent=4, ensure_ascii=False)
with open('ok.csv', mode='w', encoding='utf8') as okFile:
    w = csv.writer(okFile)
    w.writerows((i[0].replace('\n','\\n'), i[1].replace('\n','\\n')) for i in data.items())