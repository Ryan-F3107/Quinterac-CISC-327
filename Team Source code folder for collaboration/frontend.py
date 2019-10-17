import sys

class Frontend():

    def __init__(self,accountNumber):
        self.accountNumber = accountNumber

    def fileRead(self):
        accountsFileDir = sys.argv[1]
        with open(accountsFileDir) as accountsFile:
           self.accountsList = accountsFile.read().splitlines()
        return self.accountsList
    '''
    def __str__(self):
        return str(self)
    '''
    def writeToFile(self,tranCode,toAcctNum,amountCent,fromAcctNum,acctName):
        if toAcctNum is None:
            toAcctNum = "0000000"
            #print(toAcctNum)
        if amountCent is None:
            amountCent = "000"
            #print(amountCent)
        if fromAcctNum is None:
            fromAcctNum = "0000000"
            #print(fromAcctNum)
        if acctName is None:
            acctName = "***"
            #print(acctName)

        file = open(sys.argv[2],"w")
        file.write(tranCode + " " + toAcctNum + " " + amountCent + " " + fromAcctNum + " " + acctName) #END WITH EOS

    #if toacct is Null, set to 7 0s
    #ammount if null, is 000
    #from acct is Null, 7 0s
    # if account name is null its ***

    #compares if the given account number is valid or not,checks with the account number present in the file
    def compare(self,other):
        for i in self.accountsList:
            if i == str(other.accountNumber):
                return True
        return False

class Withdraw(Frontend):
    def __init__(self,accountNumber,amount):
        super().__init__(accountNumber)
        self.amount = int(amount)
    #Checks if the person has entered the valid number to deposit
    def checkAmount(self):
        if self.amount >= 0 and self.amount <= 99999999 :
            return True
        else:
            print("Invalid amount !")
            return False

class Deposit(Frontend):
    def __init__(self,accountNumber,amountDeposit):
        super().__init__(accountNumber)
        self.amountDeposit = int(amountDeposit)

    def checkAmount(self):
        if self.amountDeposit >= 0 and self.amountDeposit <= 99999999 :
            return True
        else:
            print("Invalid amount !")
            return False

def main():
    f1 = Frontend(0000000)
    f1.fileRead() #used later on to check for the valid entered account !
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
        amountWithdraw = input("Enter amount to withdraw in cents: ")
        w1 = Withdraw(accountNumber, amountWithdraw)
        result1 = f1.compare(w1)
        result2 = w1.checkAmount()
        if result1 == True and result2 == True:
            w1.writeToFile("WDR",None,str(amountWithdraw),str(accountNumber),None)

            print("Making a withdraw is possible")
        else:
            print("valid account number was not entered")
        pass
    elif userInput == "deposit":
        accountNumber = input("Enter your account Number: ")
        depositAmount = input("Enter amount to deposit: ")
        d1 = Deposit(accountNumber,depositAmount)
        result1 = f1.compare(d1)
        result2 = d1.checkAmount()
        if result1 == True and result2 == True:
            d1.writeToFile("DEP", str(accountNumber), str(depositAmount), None, None)
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