import random

def ver_function(longer, digit, ctx):
    try:
        longer = int(longer)
        digit = int(digit)
    except:
        await ctx.send('數值輸入錯誤 請聯繫機器人擁有者')
    else:
        while True:
            ch_l = []
            digit_long = digit
            digit_num = int('F'*digit, 16)
            for i in range(longer):
                ch_l.append(str(hex(random.randint(0, digit_num)).replace('0x', '')).zfill(digit_long))
            code = '-'.join(ch_l)
            await ctx.send(code)