"""
CISC 327 - Assignment 2
Authors:
        Anna Chulukov, 17avc2@queensu.ca, 20082947
        Faranak Sharifi, 17fsb@queensu.ca, 20068900
        Marwan ElKhodary, m.elkhodary@queensu.ca, 20022212
        Ryan Fernandes, 17rf@queensu.ca, 20067569

Due: Saturday, October 18th, 2019

The intention of this program is to perform the front end task following the requirements and constrains.
The input files are "your_account_list_file.txt" (the valid accounts list) and "your_transaction_summary.txt" (which remains empty); both taken in as
command line arguments. The expected output file is the transaction file with the transaction summary of all the transactions performed and
ending with an EOS (End of Session)
"""
import sys  # used to take in parameters for the program

transactionCodes = []  # global variable, a list of transaction codes that are happening in a session

'''
This function opens the directory supplied by the second argument to this program and returns a list of valid 
accounts 
'''


def readFile():
    accountsFileDir = sys.argv[1]
    with open(accountsFileDir) as accountsFile:
        accountsList = accountsFile.read().splitlines()
    return accountsList  # returns the valid account numbers in a form of a list


'''
This function carries out the login transaction and has no parameters but returns the privilege requested by the 
user
'''


def login():
    privilege = input("Please enter type of session (atm or agent): ").lower()
    if privilege == "atm":
        return privilege
    elif privilege == "agent":
        return privilege    # Returns the type of privilege, to be used in various types of transaction


'''
This function carries out the create account transaction by taking in the account list and user privilege as 
parameters 
'''


def createAcct(accountsList, privilege):
    if privilege == "atm":
        print("You cannot create an account while logged in as an atm user")
        return None  # error case, end the transaction
    else:
        accountNum = input("Please enter an account number: ")
        if len(accountNum) == 7 and accountNum[0] != '0':  # account number must be exactly 7 characters and not start
            # with 0
            if accountNum in accountsList:
                print("You cannot create an account that has been already created")
                return None  # error case, end the transaction
        else:
            print(
                "You must create an account with an account number that is exactly 7 decimal digits, not beginning "
                "with 0")
            return None  # error case, end the transaction
        accountName = input("Please enter an account name: ")
        if 3 < len(accountName) < 30 and accountName.isalnum() and \
                accountName[0] != " " and \
                accountName[-1] != " ":  # the constraints given in lecture for the accountName
            storeTransactionCode("NEW", None, None, accountNum, accountName)  # stores the transaction code for this
            # transaction
            logout()  # after creating an account you must logout


'''
This function carries out the withdraw transaction by taking in the account list and privilege type as the parameters.
'''


def withdraw(accountList, privilege):
    accountNumber = input("Enter your account Number: ")
    if accountNumber in accountList:
        amountWithdraw = input("Enter amount to withdraw in cents: ")
        if int(amountWithdraw) > 100000 and privilege == "atm":  # constraints for the amount to withdraw
            print("You cannot withdraw this amount as an atm user")
            return None
        elif int(amountWithdraw) > 99999999:  # more constraints for the amount to withdraw
            print("You cannot withdraw this amount")
        else:
            print("You withdrew $" + str(int(amountWithdraw) / 100) + " from " + str(
                accountNumber))  # print for the user
            storeTransactionCode("WDR", None, str(amountWithdraw), str(accountNumber),
                                 None)  # store the transaction code
    else:
        print("Your account number is not valid")
        return None


'''
This function carries out the deposit transaction by taking in the account list and privilege as parameters
'''


def deposit(accountList, privilege):
    accountNumber = input("Enter your account Number: ")
    if accountNumber in accountList:
        amountDeposit = input("Enter amount to deposit in cents: ")
        if int(amountDeposit) > 200000 and privilege == "atm":  # constraints for the amount to deposit
            print("You cannot deposit this amount as an atm user")
            return None
        elif int(amountDeposit) > 99999999:
            print("You cannot deposit this amount")
        else:
            print("You deposited $" + str(int(amountDeposit) / 100) + " to " + str(accountNumber))  # print for the user
            storeTransactionCode("DEP", str(accountNumber), str(amountDeposit), None, None) # store the transaction code
    else:
        print("Your account number is not valid")
        return None


'''
This function carries out the transfer transaction by taking in the account list and privilege as parameters
'''


def transfer(accountList, privilege):
    fromAccountNumber = input("Enter your account Number: ")
    toAccountNumber = input("Enter the account number that you are transferring to: ")
    if fromAccountNumber in accountList and toAccountNumber in accountList:
        amountTransfer = input("Enter amount to transfer in cents: ")
        if int(amountTransfer) > 1000000 and privilege == "atm":
            print("You cannot transfer this amount as an atm user")
            return None
        elif int(amountTransfer) > 99999999:
            print("You cannot transfer this amount")
        else:
            print("You transferred $" + str(int(amountTransfer) / 100) + " to " + str(toAccountNumber))
            storeTransactionCode("XFR", str(toAccountNumber), str(amountTransfer), str(fromAccountNumber), None)
    else:
        print("Your account number or the account number that you are trying to transfer to is not valid")
        return None


'''
This function carries out the delete account transaction by taking in the account list and privilege as parameters
'''


def deleteAcct(accountsList, privilege):
    if privilege == "atm":
        print("You cannot delete an account while logged in as an atm user")
        return None
    else:
        accountNum = input("Please enter an account number you are trying to delete: ")
        if accountNum not in accountsList:
            print("You cannot delete an account that hasn't been already created")
            return None
        accountName = input("Please enter an account name: ")
        if 3 < len(accountName) < 30 and accountName.isalnum() and \
                accountName[0] != " " and accountName[-1] != " ":
            storeTransactionCode("DEL", None, None, accountNum, accountName)


'''
This function carries out the logout transaction, it does not take in any parameters, it writes to the transaction summary
file from the global list created called "transactionCodes" and writes "EOS" at the end of the transaction Summary File. 
'''


def logout():
    transactionSummaryFile = open(sys.argv[2], "a+")
    for i in transactionCodes:
        transactionSummaryFile.write(i + "\n")
    transactionSummaryFile.write("EOS")
    print("Your session has ended")


'''
This function writes the transaction summary line to the global list, and it's used by all the transactions except
login and logout.
'''


def storeTransactionCode(tranCode, toAcctNum, amountCent, fromAcctNum, acctName):
    if toAcctNum is None:
        toAcctNum = "0000000"
    if amountCent is None:
        amountCent = "000"
    if fromAcctNum is None:
        fromAcctNum = "0000000"
    if acctName is None:
        acctName = "***"
    #   Writes the Transaction Summary File to the appropriate folder
    transactionCodeStr = tranCode + " " + toAcctNum + " " + amountCent + " " + fromAcctNum + " " + acctName
    transactionCodes.append(transactionCodeStr)


'''
Main runs the whole program, it contains a loop that allows the user to perform transactions, and the program only ends 
when the user creates a new account or logs out.
'''


def main():
    global transactionCodes  # needed for to use the global variable
    session = True  # needed to run the loop, unless it turns false
    userLogin = input("Please enter the command 'login': ").lower()
    if userLogin == "login":
        privilege = login()
        accountsList = readFile()  # gets a list of valid account numbers
        count = 1   # lets the user know how many transactions that they have performed
        while session is True:
            userInput = input("\n" + "Transaction " + str(count) + " - Please enter type of transaction: ").lower()  #  converts input into lower case
            if userInput == "createacct":
                createAcct(accountsList, privilege)
                session = False  #   session ends since after creating an account the user cannot perform any other transaction in the same session,based on the constraint.
                count += 1
            elif userInput == "withdraw":
                withdraw(accountsList, privilege)
                count += 1
            elif userInput == "deposit":
                deposit(accountsList, privilege)
                count += 1
            elif userInput == "transfer":
                transfer(accountsList, privilege)
                count += 1
            elif userInput == "deleteacct":
                deleteAcct(accountsList, privilege)
                count += 1
            elif userInput == "logout":
                logout()
                session = False
    else:
        print("You must login to start the session, please restart the program ")


main()
