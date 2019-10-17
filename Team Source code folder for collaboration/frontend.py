import sys
#import withdraw

class Frontend():

    def __init__(self,accountNumber):
        self.accountNumber = accountNumber

    def fileRead(self):
        accountsFileDir = sys.argv[1]
        with open(accountsFileDir) as accountsFile:
           self.accountsList = accountsFile.read().splitlines()
        return self.accountsList
    '''
    def validAccount(accountNum):
        validAccountList = fileRead()
        for i in validAccountList:
            if accountNum == validAccountList[int(i)]:
                print("It\'s legit")
                return True
        return False
    '''
    '''
    def __str__(self):
        return str(self)
    '''
    #compares if the given account number is valid or not,checks with the account number present in the file
    def compare(self,other):
        for i in self.accountsList:
            if i == str(other.accountNumber):
                return True
        return False

class Withdraw(Frontend):
    def __init__(self,accountNumber,amount):
        super().__init__(accountNumber)
        self.amount = amount

class Deposit(Frontend):
    def __init__(self,accountNumber,amountDeposit):
        super().__init__(accountNumber)
        self.amountDeposit = amountDeposit
def main():
    f1 = Frontend(0000000)
    f1.fileRead()
    print(f1.fileRead())
    userIn = input("enter your choice: ")
    userInput = userIn.lower()
    if userInput == "login":
        print("login works")
        pass
        #login
    elif userInput == "createaccount":
        pass
    elif userInput == "withdraw":
        accountNumber = input("Enter your account Number: ")
        amountWithdraw = input("Enter amount to withdraw: ")
        w1 = Withdraw(accountNumber, amountWithdraw)
        result = f1.compare(w1)
        if result == True:
            print("Making a withdraw is possible")
        else:
            print("valid account number was not entered")
        pass
    elif userInput == "deposit":
        accountNumber = input("Enter your account Number: ")
        depositAmount = input("Enter amount to deposit: ")
        d1 = Deposit(accountNumber,depositAmount)
        result = f1.compare(d1)
        if result == True:
            print("Making a deposit to this account is possible")
        else:
            print("invalid entered account number")
        pass
    elif userInput == "transfer":
        pass
    elif userInput == "deleteaccount":
        pass
    elif userInput == "logout":
        pass

main()