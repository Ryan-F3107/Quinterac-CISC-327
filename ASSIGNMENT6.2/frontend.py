#!/usr/bin/python3
import datetime
"""
CISC 327 - Assignment 2 and modified in Assignment 3 to pass all the front_end test cases
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
import datetime #used to add the date and time of the creation of transaction summary files
transactionCodes = []  # global variable, a list of transaction codes that are happening in a session

'''
This function opens the directory supplied by the second argument to this program and returns a list of valid 
accounts 
'''


def readFile():
    accountsFile = open("valid_account_list.txt", "r")
    accountsList = accountsFile.read().splitlines()
    return accountsList  # returns the valid account numbers in a form of a list


'''
This function carries out the login transaction and has no parameters but returns the privilege requested by the 
user
'''


def login():
    privilege = input("Please enter type of session (atm or agent): ").lower()
    while (privilege != "atm") and (privilege != "agent"):
        print("Wrong input. Please print atm or agent")
        privilege = input("Please enter type of session (atm or agent): ").lower()
    if privilege == "atm":
        return privilege
    elif privilege == "agent":
        return privilege  # Returns the type of privilege, to be used in various types of transaction


'''
This function carries out the create account transaction by taking in the account list and user privilege as 
parameters 
'''


def createAcct(accountsList, privilege):
    if privilege == "atm":
        print("You cannot create an account while logged in as an atm user")
        return False  # error case, end the transaction
    else:
        accountNum = input("Please enter an account number: ")
        # account number must be exactly 7 characters and not start with 0
        if len(accountNum) == 7 and accountNum[0] != '0':
            if accountNum in accountsList:
                print("You cannot create an account that has been already created")
                return False  # error case, end the transaction
        else:
            print(
                "You must create an account with an account number that is exactly 7 decimal digits, not beginning "
                "with 0")
            return False  # error case, end the transaction
        accountName = input("Please enter an account name: ")
        accountNameNoSpace = accountName.replace(" ", "")  # Removes all the spaces from the string
        # Checks if the original string satisfies the conditions from Transaction Summary File
        if 3 <= len(accountName) <= 30 and accountName[0] != " " and accountName[-1] != " " and \
                accountNameNoSpace.isalnum():  # checks if the string is alphanumeric
            storeTransactionCode("NEW", accountNum, None, None, accountName) #this line was changed in the new iteration
            return True
        else:
            print(
                "You must enter an alphanumeric account name that is between 3 and 30 characters and doesn't begin "
                "or end with whitespaces")
            return False


'''
This function carries out the withdraw transaction by taking in the account list and privilege type as the parameters.
'''


def withdraw(accountList, privilege):
    accountNumber = input("Enter your account Number: ")
    if accountNumber.isdigit():
        if accountNumber in accountList:
            amount = input("Enter amount to withdraw in cents: " or "0")
            if amount.isdigit():
                amountWithdraw = int(amount)
                if amountWithdraw > 100000 and privilege == "atm":  # constraints for the amount to withdraw
                    print("You cannot withdraw this amount as an atm user")
                    return None
                elif amountWithdraw > 99999999:  # more constraints for the amount to withdraw
                    print("You cannot withdraw this amount")
                else:
                    # print for the user
                    print("You withdrew $" + str(amountWithdraw / 100) + " from " + str(accountNumber))
                    # store the transaction code
                    storeTransactionCode("WDR", None, str(amountWithdraw), str(accountNumber), None)
            else:
                print("You must enter a numeric value for your withdrawal amount")
        else:
            print("Your account number is not valid")
            return None
    else:
        print("You must enter a numeric value for your account number")
        return None


'''
This function carries out the deposit transaction by taking in the account list and privilege as parameters
'''


def deposit(accountList, privilege):
    accountNumber = input("Enter your account Number: ")
    if accountNumber.isdigit():
        if accountNumber in accountList:
            amount = input("Enter amount to deposit in cents: " or "0")
            if amount.isdigit():
                amountDeposit = int(amount)
                if amountDeposit > 200000 and privilege == "atm":  # constraints for the amount to withdraw
                    print("You cannot deposit this amount as an atm user")
                    return None
                elif amountDeposit > 99999999:  # more constraints for the amount to withdraw
                    print("You cannot deposit this amount")
                else:
                    # print for the user
                    print("You deposited $" + str(amountDeposit / 100) + " to " + str(accountNumber))
                    # store the transaction code
                    storeTransactionCode("DEP", str(accountNumber), str(amountDeposit), None, None)
            else:
                print("You must enter a numeric value for your deposit amount")
        else:
            print("Your account number is not valid")
            return None
    else:
        print("You must enter a numeric value for your account number")
        return None


'''
This function carries out the transfer transaction by taking in the account list and privilege as parameters
'''


def transfer(accountList, privilege):
    fromAccountNumber = input("Enter your account Number: ")
    toAccountNumber = input("Enter the account number that you are transferring to: ")
    if (fromAccountNumber == toAccountNumber):
        print("Error: destination account is the same as the current account")
    elif fromAccountNumber in accountList and toAccountNumber in accountList:
        amountTransfer = input("Enter amount to transfer in cents: ")
        try:
            amountTransfer = int(amountTransfer)
            if int(amountTransfer) > 1000000 and privilege == "atm":
                print("You cannot transfer this amount as an atm user")
                return None
            elif int(amountTransfer) > 99999999:
                print("You cannot transfer this amount")
            elif int(amountTransfer) < 0:
                print("You cannot transfer negative amounts")
            elif int(amountTransfer) == 0:
                print("You cannot transfer zero")
            else:
                print("You transferred $" + str(int(amountTransfer) / 100) + " to " + str(toAccountNumber))
                storeTransactionCode("XFR", str(toAccountNumber), str(amountTransfer), str(fromAccountNumber), None)
        except ValueError:  # if value entered to be transfered is not an integer
            print("Amount entered is not valid")
            return None
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
        if len(accountNum) == 0:
            print("Account number field was left empty")
            return False
        if accountNum not in accountsList:
            print("You cannot delete an account that hasn't been already created")
            return None
        accountName = input("Please enter an account name: ")
        accountNameNoSpace = accountName.replace(" ", "")  # Removes all the spaces from the string
        # Checks if the original string satisfies the conditions from Transaction Summary File
        if 3 <= len(accountName) <= 30 and accountName[0] != " " and accountName[-1] != " " and \
                accountNameNoSpace.isalnum():  # checks if the string is alphanumeric
            storeTransactionCode("DEL", None, None, accountNum, accountName)
            return True
        else:
            print(
                "You must enter an alphanumeric account name that is between 3 and 30 characters and doesn't begin "
                "or end with whitespaces")
            return False


'''
This function carries out the logout transaction, it does not take in any parameters, it writes to the transaction summary
file from the global list created called "transactionCodes" and writes "EOS" at the end of the transaction Summary File. 
'''


def logout():
    now=datetime.datetime.now()
    time=now.strftime("%Y-%m-%d-%H-%M-%S")
    transactionSummaryFile = open("your_transaction_summary_" + time+".txt", "w")
    #transactionSummaryFile = open(sys.argv[2], "a+") #this line was changed to the line above
    for i in transactionCodes:
        transactionSummaryFile.write(i + "\n")
    transactionSummaryFile.write("EOS 0000000 000 0000000 ***\n")
    print("Your session has ended")
    another = input("Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: ")
    while True:
        if len(another) > 0 and another.isalnum():
            if another == "yes" or another == "y":
                return False
            elif another == "no" or another == "n":
                print("Thank you for using Quinterac, have a nice day!")
                transactionSummaryFile.close()
                return True
            else:
                print("You have entered an unexpected string: " + another + ". Your session has ended!")
                print("Thank you for using Quinterac, have a nice day!")
                transactionSummaryFile.close()
                return True
        else:
            print("your session has ended")
            print("Thank you for using Quinterac, have a nice day!")
            transactionSummaryFile.close()
            return True
    

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
This function runs the user session: it asks them what they want to do and calls the appropriate function,
The session runs as long as session == True and only exits the loop when logout is called.
'''


def userSession(accountsList):
    session = True  # needed to run the loop, unless it turns false
    privilege = login()
    count = 1  # lets the user know how many transactions that they have performed
    while session:
        userInput = input("\n" + "Transaction " + str(
            count) + " - Please enter type of transaction: ").lower()  # converts input into lower case
        if userInput == "createacct":
            createAcct(accountsList, privilege)
            return logout()
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
            outcome = deleteAcct(accountsList, privilege)
            if outcome is True:  # Checks if an account is successfully deleted
                return logout()  # When account is successfully deleted, the user is logout
        elif userInput == "logout":
            return logout()


'''
Main runs the whole program, it contains a loop that allows the user to perform transactions, and the program only ends 
when the user creates a new account or logs out.

[For Assignment 3, main can be called from __main__.py file, to run the program on PyCharm]
'''


def main():
    global transactionCodes  # needed for to use the global variable
    # during the day the frontend runs.
    # I am assuming day is between 6 am and 8pm (20 hours)
    # after every transaction I add 0.1 to the current time, which is about 6 minutes.
    good_to_exit = False
    accountsList = readFile()  # gets a list of valid account numbers
    while not good_to_exit:
        print("\n\nThis is a new session")
        userLogin = str(input("Please enter the command 'login': ")).lower()
        while userLogin != "login":
            print("You must login to start the session")
            userLogin = str(input("Please enter the command 'login': ")).lower()
        good_to_exit = userSession(accountsList)


main()
