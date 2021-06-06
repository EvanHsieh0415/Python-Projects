class bank:
    def __init__(self):
        self.accountDict = {}
    
    def inputCheck(self, email, password):
        if email not in self.accountDict:
            return 'EmailNotFound'
        if self.accountDict[email]['password'] != password:
            return 'PasswrodError'
        return None

    def createAccount(self, email, password, name):
        if email in self.accountDict:
            return 'EmailUsed'
        if not name:
            return 'NameNull'
        self.accountDict[email] = {'name': name, 'password': password, 'deposit': 0}
        return 'CreateSuccessful'
    
    def deleteAccount(self, email, password):
        check = Bank.inputCheck(email, password)
        if check:
            return check
        confirm = input(f'是否確定刪除{self.accountDict[email]["name"]}( True/False ): ')
        if confirm == 'True':
            del self.accountDict[email]
            return 'ActionSuccessful'
        if confirm == 'False':
            return 'ActionCancel'
        return 'UnknowAction'
    
    def saveMoney(self, email, password, amount):
        check = Bank.inputCheck(email, password)
        if check:
            return check
        if amount.isdigit():
            amount = int(amount)
            self.accountDict[email]['deposit'] += amount
            return 'SaveSuccessful'
        return 'AmountEnterError'
    
    def takeMoney(self, email, password, amount):
        check = Bank.inputCheck(email, password)
        if check:
            return check
        if amount.isdigit():
            amount = int(amount)
            if self.accountDict[email]['deposit'] < amount:
                return 'DepositNotEnough'
            self.accountDict[email]['deposit'] -= amount
            return 'TakeSuccessful'
        return 'AmountEnterError'
    
    def showDeposit(self, email, password):
        check = Bank.inputCheck(email, password)
        if check:
            return check
        return self.accountDict[email]['deposit']

Bank = bank()

def output(string:str):
    stringDict = {
        # Null
        'EmailNull': '[Error] 請輸入E-mail',
        'PasswordNull': '[Error] 請輸入密碼',
        'NameNull': '[Error] 請輸入帳戶名稱',
        'AmountNull': '[Error] 請輸入金額',
        
        # Account Error
        'EmailNotFound': '[Error] 資料庫內無此E-mail',
        'EmailUsed': '[Error] E-mail已使用',
        'PasswrodError': '[Error] 密碼輸入錯誤',

        # Action
        'ActionSuccessful': '操作成功',
        'ActionCancel': '[Error] 操作取消',
        'UnknowAction': '[Error] 未知的操作',
        'SaveSuccessful': '成功存入銀行帳戶',
        'TakeSuccessful': '取款成功',

        # Amount
        'AmountEnterError': '[Error] 金額輸入錯誤',

        # Deposit
        'DepositNotEnough': '[Error] 存款不足',

        # Account
        'CreateSuccessful': '帳戶創建成功'
    }
    return stringDict[string]

def line():
    print('='*100)

line()
print('歡迎來到芒果銀行！！！\n若您是新用戶，請先創建帳戶 輸入"create account"）\n刪除帳戶 請輸入"delete account"\n存款 請輸入"save money"\n取款 請輸入"take money"\n離開此系統 請輸入"leave"')
line()

tragger = True
while tragger:
    action = input('輸入您要進行的操作: ')
    if not action:
        print('[Error] 請輸入操作名稱')
        line()
        continue
    if action not in ('create account', 'delete account', 'save money', 'take money', 'leave'):
        print('[Error] 請輸入正確的操作')
        line()
        continue
    if action == 'leave':
        print('程式關閉')
        tragger = False
    if action in ('create account', 'delete account', 'save money', 'take money'):
        email = input('請輸入E-mail: ')
        if not email:
            print(output('EmailNull'))
            line()
            continue
        password = input('請輸入密碼: ')
        if not password:
            print(output('PasswordNull'))
            line()
            continue
        if action in ('save money', 'take money'):
            amount = input('請輸入金額: ')
            if not amount:
                print(output('AmountNull'))
                line()
                continue
        if action == 'create account':
            name = input('請輸入使用者名稱: ')
            out = Bank.createAccount(email, password, name)
        elif action == 'delete account':
            out = Bank.deleteAccount(email, password)
        elif action == 'save money':
            out = Bank.saveMoney(email, password, amount)
        elif action == 'take money':
            out = Bank.takeMoney(email, password, amount)
        print(output(out))
        if out in ('SaveSuccessful', 'TakeSuccessful', 'DepositNotEnough'):
            print(f'存款餘額: {Bank.showDeposit(email, password)}')
    line()

input('Press any key to continue . . .')