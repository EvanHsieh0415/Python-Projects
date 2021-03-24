'''
Made By Mango
Discord: YT Mango#4092
Versoin : 1.8
'''
import random
import json

with open('.\\setting.json', mode='r', encoding='utf8') as file:
    data = json.load(file)
Min, Max = data['Min'], data['Max']

print('Welcome to Guess Number.  Please enter max number and min number.\n')

while True:
    ans_list = []
    while True: 
        Min = input(f'Min Number (Default Value: {Min}) : ') or Min
        Max = input(f'Max Number (Default Value: {Max}) : ') or Max
        try:
            Max, Min = int(Max), int(Min)
        except:
                print('Max Number and Min Number must be numbers.  Please re-enter Max Number and Min Number\n')
        else:
            if Max < Min:
                print('Max Number must be higher than Min Number.  Please re-enter Max Number and Min Number.\n')
            else:
                print('Enter Correct.  Let us play now!\n')
                break


    ans = random.randint(Min, Max)

    while True:
        try:
            input_ans = int(input('Guess a number: '))
        except:
            print('Please enter a number\n')
        else:
            print()
            input_ans = int(input_ans)
            if Max >= input_ans and Min <= input_ans  :
                ans_list.append(input_ans)
                if input_ans != ans:
                    if input_ans > ans:
                        Max = input_ans
                        print(f'Too big, Now range is {Min} to {Max}\n')
                    else:
                        Min = input_ans
                        print(f'Too Small, Now range is {Min} to {Max}\n')
                    cnum = round((Max+Min)/2)
                    print(f'Center number is {cnum}')
                else:
                    print(f'Game End, You got the number.  The number is {ans}\n')
                    break
            else:
                print('The number entered must be within the range.  Please re-enter the numer\n')

    print(f'guess {len(ans_list)} time(s)')
    print(f'The number is {ans}')
    print(f'guess history: {ans_list}\n')

    keep = input('Play again?(enter "Y" or "y" to play again) > ')
    if keep in data['again']:
        print('\n==================== Next Game ====================\n')
    else:
        print('\n==================== Game End ====================')
        break

input()