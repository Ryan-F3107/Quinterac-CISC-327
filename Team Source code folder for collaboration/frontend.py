import sys
import withdraw
'''
class Frontend:
    def __init__(self,accountNum):#constructor
        self.accountNum = accountNum
'''
def fileRead():
    accountsFileDir = sys.argv[1]
    with open(accountsFileDir) as accountsFile:
       accountsList = accountsFile.read().splitlines()
    return accountsList

def validAccount(accountNum):
    validAccountList = fileRead()
    for i in validAccountList:
        if accountNum == validAccountList[int(i)]:
            print("It\'s legit")
            return True
    return False
    '''
    def __str__(self):
        return str(self)
    '''

def main():
    print("It works")
    '''
    ryan = Withdraw(1234567,2000)
    ryan.fileRead()
   # ryan.__str__()
    '''
    userIn = input("enter your choice: ")
    userInput = userIn.lower()
    if userInput == "login":
        print("login works")
        pass
        #login
    elif userInput == "createaccount":
        pass
    elif userInput == "withdraw":
        accountNumber = input("Enter your account Number")
        amountWithdraw = input("Enter amount to withdraw")
        withdraw.check(accountNumber,amountWithdraw)
        pass
    elif userInput == "deposit":
        pass
    elif userInput == "transfer":
        pass
    elif userInput == "deleteaccount":
        pass
    elif userInput == "logout":
        pass

main()