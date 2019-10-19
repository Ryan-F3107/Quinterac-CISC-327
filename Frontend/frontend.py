'''
CISC 327, Assignment 2
'''
import sys

class Frontend:

    def __init__(self, accountNumber,amount):
        self.accountNumber = accountNumber
        self.amount = amount

    def getAccount(self):
        return str(self.accountNumber)

    def getAmount(self):
        return str(int(self.amount)/100)

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
        file = open(sys.argv[2], "a+")
        file.write(tranCode + " " + toAcctNum + " " + amountCent + " " + fromAcctNum + " " + acctName + "\n") # END WITH EOS

    #   compares if the given account number is valid or not,checks with the account number present in the file
    def compare(self, other):
        for i in self.accountsList:
            if i == str(other.accountNumber):
                return True
        return False

    def checkAmount(self):
        if int(self.amount) >= 0 and int(self.amount) <= 99999999:
            return True
        else:
            print("Invalid amount !")
            return False


class Withdraw(Frontend):
    def __init__(self, accountNumber, amount):
        super().__init__(accountNumber, amount)
    def execution(self):
        accountNumber = input("Enter your account Number: ")
        amountWithdraw = input("Enter amount to withdraw in cents: ")
        w1 = Withdraw(accountNumber, amountWithdraw)
        w1.fileRead()
        result1 = w1.compare(w1)
        result2 = w1.checkAmount()
        if result1 is True and result2 is True:
            w1.writeToFile("WDR", None, str(amountWithdraw), str(accountNumber), None)
            print("You withdrew " + "$" + w1.getAmount() + " from " + w1.getAccount())
        else:
            print("valid account number was not entered")

class Deposit(Frontend):
    def __init__(self, accountNumber, amountDeposit):
        super().__init__(accountNumber,amountDeposit)

    def execution(self):
        accountNumber = input("Enter your account Number: ")
        depositAmount = input("Enter amount to deposit: ")
        d1 = Deposit(accountNumber, depositAmount)
        d1.fileRead()
        result1 = d1.compare(d1)
        result2 = d1.checkAmount()
        if result1 is True and result2 is True:
            d1.writeToFile("DEP", str(accountNumber), str(depositAmount), None, None)
            print("You deposited " + "$" + d1.getAmount() + " to " + d1.getAccount())
        else:
            print("invalid entered account number")

class Transfer(Frontend):
    def __init__(self, fromAccountNumber, amountTransfer, toAccountNumber):
        super().__init__(fromAccountNumber,amountTransfer)
        self.toAccountNumber = toAccountNumber

    def compareAccounts(self, fromAccountNumber,toAccountNumber):
        if fromAccountNumber in self.accountsList and toAccountNumber in self.accountsList:
            return True
        return False

    def execution(self):
        fromAccountNumber = input("Enter your account Number: ")
        toAccountNumber = input("Enter the account number that you are transferring to: ")
        amountTransfer = input("Enter amount to transfer: ")
        t1 = Transfer(fromAccountNumber, amountTransfer, toAccountNumber)
        t1.fileRead()
        if t1.compareAccounts(fromAccountNumber, toAccountNumber) and t1.checkAmount():
            t1.writeToFile("XFR", str(toAccountNumber), str(amountTransfer), str(fromAccountNumber), None)
            print("You transferred " + "$" + t1.getAmount() + " to " + str(toAccountNumber))
        else:
            print("invalid entered account number(s) or amount")


def main():
    userIn = input("Enter your choice: ")
    userInput = userIn.lower()
    if userInput == "login":
        print("login works")
        pass
    elif userInput == "createaccount":
        pass
    elif userInput == "withdraw":
        w0 = Withdraw(0000000, 000) # Initialize the withdraw object to use the execution function
        w0.execution()
    elif userInput == "deposit":
        d0 = Deposit(0000000, 000) # Initialize the deposit object to use the execution function
        d0.execution()
    elif userInput == "transfer":
        t0 = Transfer(0000000, 000, 0000000) # Initialize the transfer object to use the execution function
        t0.execution()
        pass
    elif userInput == "deleteaccount":
        pass
    elif userInput == "logout":
        pass

main()