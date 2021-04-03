import random

def verify(mode:str='info', length=16):
    modeList = ['info', 'get']
    if mode in modeList:
        if mode == 'info':
            output = 'info'
        elif mode == 'get':
            if length.isdigit():
                codes = ''
                for i in range(int(length)):
                    codes += str(random.randint(0,9))
                output = codes
            else:
                output = '[ERROR] length must be an integer'
    else:
        output = '[ERROR] mode not found'
    return output
