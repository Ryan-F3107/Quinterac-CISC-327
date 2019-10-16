import frontend
'''
withdraw transaction class

class Withdraw(Frontend):
    def __init__(self,accountNumber,amount):
        super().__init__(accountNumber)
        self.amount = amount
'''
def check(accountNumber,moneyDepo):
    result1 = frontend.validAccount(accountNumber)

    #go through every line in TSF,ctr = 0,
    #line starting with DEP;TRANSFER(from),ctr will increase
    #line starting with
