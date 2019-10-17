import sys

class Frontend:

    def __init__(self, accountNumber):
        self.accountNumber = accountNumber

    def getAccount(self):
        return str(self.accountNumber)

    def fileRead(self):
        accountsFileDir = sys.argv[1]
        with open(accountsFileDir) as accountsFile:
           self.accountsList = accountsFile.read().splitlines()
        return self.accountsList

    def writeToFile(self, tranCode, toAcctNum, amountCent, fromAcctNum, acctName):
        if toAcctNum is None:
            toAcctNum = "0000000"
        if amountCent is None:
            amountCent = "000"
        if fromAcctNum is None:
            fromAcctNum = "0000000"
        if acctName is None:
            acctName = "***"
        #   Writes the Transaction Summary File to the appropriate folder
        file = open(sys.argv[2], "w+")
        file.write(tranCode + " " + toAcctNum + " " + amountCent + " " + fromAcctNum + " " + acctName + "\n" + "EOS") # END WITH EOS

    #   compares if the given account number is valid or not,checks with the account number present in the file
    def compare(self, other):
        for i in self.accountsList:
            if i == str(other.accountNumber):
                return True
        return False

class Withdraw(Frontend):
    def __init__(self, accountNumber, amount):
        super().__init__(accountNumber)
        self.amount = int(amount)
    #   Checks if the person has entered the valid number to deposit
    def getAmount(self):
        return str(self.amount/100)
    def checkAmount(self):
        if self.amount >= 0 and self.amount <= 99999999:
            return True
        else:
            print("Invalid amount !")
            return False

class Deposit(Frontend):
    def __init__(self, accountNumber, amountDeposit):
        super().__init__(accountNumber)
        self.amountDeposit = int(amountDeposit)

    def getAmount(self):
        return str(self.amountDeposit/100)

    def checkAmount(self):
        if self.amountDeposit >= 0 and self.amountDeposit <= 99999999:
            return True
        else:
            print("Invalid amount !")
            return False

def main():
    '''
    f1 = Frontend(0000000) [FIXED ISSUE, CAN BE DELETED ]
    f1.fileRead() #used later on to check for the valid entered account !
    '''
    userIn = input("Enter your choice: ")
    userInput = userIn.lower()
    if userInput == "login":
        print("login works")
        pass
    elif userInput == "createaccount":
        pass
    elif userInput == "withdraw":
        accountNumber = input("Enter your account Number: ")
        amountWithdraw = input("Enter amount to withdraw in cents: ")
        w1 = Withdraw(accountNumber, amountWithdraw)
        w1.fileRead()
        result1 = w1.compare(w1)
        result2 = w1.checkAmount()
        if result1 is True and result2 is True:
            w1.writeToFile("WDR",None,str(amountWithdraw),str(accountNumber),None)
            print("You withdrew " + "$" + w1.getAmount() + " from " + w1.getAccount())
        else:
            print("valid account number was not entered")
        pass
    elif userInput == "deposit":
        accountNumber = input("Enter your account Number: ")
        depositAmount = input("Enter amount to deposit: ")
        d1 = Deposit(accountNumber,depositAmount)
        d1.fileRead()
        result1 = d1.compare(d1)
        result2 = d1.checkAmount()
        if result1 is True and result2 is True:
            d1.writeToFile("DEP", str(accountNumber), str(depositAmount), None, None)
            print("You deposited " + "$" + d1.getAmount() + " to " + d1.getAccount())
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