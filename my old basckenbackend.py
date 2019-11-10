"""
CISC 327 - Assignment 4

This program simulates the backend office of Quinterac.

The input files are the Transaction Summary File and the Master Account File
The generated output file is the New Master Account file and the Valid Account List File

The program intends to take in the two input files, modify the master account file based on the content from
the Merged Transaction Summary File and generate the New Valid Account list and new master account list,
for this program, it will run starting from the main function within the backend.py file.

Authors:
        Anna Chulukov, 17avc2@queensu.ca, 20082947
        Faranak Sharifi, 17fsb@queensu.ca, 20068900
        Marwan ElKhodary, m.elkhodary@queensu.ca, 20022212
        Ryan Fernandes, 17rf@queensu.ca, 20067569
"""

import sys


'''This function takes in the first argument of the program, the transaction summary file, and returns the 
transactions as a list of strings '''


def readTransFile():
    merged_TSF = sys.argv[1]
    with open(merged_TSF) as transactionFile:
        transactionList = transactionFile.read().splitlines()
    return transactionList  # returns transactions as individual strings in a list


'''This function takes in the second argument of the program, the master accounts file, and returns it as a 
dictionary '''
def readMaster():
    masterAccountDict = {}
    masterFileDir = sys.argv[2]
    with open(masterFileDir) as masterFile:
        masterList = masterFile.read().splitlines()
        for line in masterList:
            eachAccount = line.split()
            accountNum = eachAccount[0]
            accountBalance = eachAccount[1]
            accountName = eachAccount[2]
            try:    # checks if the values are of the right data type
                int(accountNum)
                int(accountBalance)
            except ValueError:
                exit("Fatal ERROR: accountNum and/or accountBalance are not integers")
            masterAccountDict[accountNum] = [accountBalance, accountName]  # accountNum serve as the key and the values
            # are a list of accountBalance and accountName
    return masterAccountDict  # returns the accounts as objects in a list


'''This function modifies and maintains the master accounts file in descending order and 
adds the content from the master account dictionary into the file with the right format
'''


def writeMaster(masterAccountDict):
    masterAccountFile = open(sys.argv[2], "w")
    for accountNum in sorted(masterAccountDict.keys()):
        masterAccountFile.write(accountNum + " " + masterAccountDict[accountNum][0] + " " +
                                masterAccountDict[accountNum][1] + "\n")


'''This function creates new valid account list and adds the content from the master account dictionary into the file 
with the right format'''


def newValidAccountList(masterAccountDict):
    validAccount = open("valid_account_list.txt", "w+")
    for accountNum in masterAccountDict:
        validAccount.write(accountNum + "\n")
    validAccount.write("0000000")


'''This function takes in the master account dictionary, an account number and an amount and update's that user's 
account with the amount they want to deposit'''


def deposit(masterAccountDict, accountNum, amount):
    # see how much money they have
    moneyHave = masterAccountDict[accountNum][0]
    # add it to the amount they want to deposit
    moneyHave = int(moneyHave) + int(amount)
    masterAccountDict[accountNum][0] = str(moneyHave)   #   masterAccountDict's modified based on TransactionSummaryFile
    return masterAccountDict

'''This function takes in the master account dictionary, an account number and an amount and update's that user's 
account with the amount they want to withdraw'''


def withdraw(masterAccountDict, accountNum, amount):
    # see how much money they have
    moneyHave = masterAccountDict[accountNum][0]  # check if this should be toAccount or accountNum

    # subtract it by the amount they want to withdraw
    moneyHave = int(moneyHave) - int(amount)
    if moneyHave < 0:
        print("Do not have enough funds!")
        return masterAccountDict
    # store new amount of money back into the dictionary
    masterAccountDict[accountNum][0] = str(moneyHave)
    return masterAccountDict

'''This function takes in the master account dictionary, an account that money is being transferred to and an account 
that money is being transferred from as well as the amount and updates the user's details post-transfer '''


def transfer(masterAccountDict, destAccount, fromAccount, amount):
    # get money in first account
    moneyHave = masterAccountDict[fromAccount][0]

    # subtract how much they have to how much they want to transfer
    moneyHave = int(moneyHave) - int(amount)
    if moneyHave < 0:
        print("Do not have enough funds!")
        return masterAccountDict

    # store new amount of money back into the dictionary
    masterAccountDict[fromAccount][0] = str(moneyHave)

    # add to money they have to how much they were transferred
    moneyHave2 = int(masterAccountDict[destAccount][0]) + int(amount)

    # store new amount of money back into the dictionary
    masterAccountDict[destAccount][0] = str(moneyHave2)
    return masterAccountDict

'''This function takes in the master account dictionary, an account Number and account name 
and updates the master account dictionary, adding a new account into the master accounts file
'''


def createAccount(masterAccountDict,accountNum,accountName):
    if accountNum in masterAccountDict:
        print("Please enter new account number, this one is taken!")
    else:
        # Since no other transaction is accepted after an account is created, the new accounts balance is $0.00
        masterAccountDict[accountNum] = ["000", accountName]
    return masterAccountDict

'''This function takes in the master account dictionary, an account Number and account name 
and updates the master account dictionary, removing the deleted account from the master accounts file
'''


def deleteAccount(masterAccountDict,accountNum,accountName):
    accountNameMaster = masterAccountDict[accountNum][1]
    accountBalance = masterAccountDict[accountNum][0]
    if accountNameMaster != accountName:
        print("names do not match!")
    #elif int(accountBalance) != 0:
    #    print("account balance is not zero, it has to be zero!")
    else:
        print("deleting account")
        del masterAccountDict[accountNum]   #   Deletes the account from the master account dictionary
    return masterAccountDict

def main():
    # read dictionary that has account number, account balance and account name
    masterAccountDict = readMaster()

    # read transactions in a list
    transactionList = readTransFile()
    for i in masterAccountDict:
        print(masterAccountDict[i])
    for x in transactionList:  # goes through a list of transactions
        eachTransaction = x.split()
        #  Each part of the Transaction Summary line is assigned a variable.
        transCode = eachTransaction[0]
        toAccount = eachTransaction[1]
        amount = eachTransaction[2]
        fromAccount = eachTransaction[3]
        accountName = eachTransaction[4]
        if transCode != "NEW" and transCode != "EOS":  #   Checks if account exists or not
            if fromAccount == "0000000" and toAccount == "0000000":
                print("There is no such account: " + fromAccount)
                exit("Fatal ERROR")
        if transCode == "DEP":
            print("dep")
            print(masterAccountDict[toAccount])
            masterAccountDict=deposit(masterAccountDict, toAccount, amount)
            print(masterAccountDict[toAccount])
        elif transCode == "WDR":
            print("wdr")
            print(masterAccountDict[fromAccount])
            masterAccountDict=withdraw(masterAccountDict, fromAccount, amount)
            print(masterAccountDict[fromAccount])
        elif transCode == "XFR":
            print("xfr")
            print(masterAccountDict[fromAccount])
            print(masterAccountDict[toAccount])
            masterAccountDict=transfer(masterAccountDict, toAccount, fromAccount, amount)
            print(masterAccountDict[fromAccount])
            print(masterAccountDict[toAccount])
        elif transCode == "NEW":
            print("new")
            masterAccountDict=createAccount(masterAccountDict, toAccount, accountName)
            print(masterAccountDict[toAccount])
            print(toAccount)
        elif transCode == "DEL":
            print("del")
            print(masterAccountDict[toAccount])
            print(toAccount)
            masterAccountDict=deleteAccount(masterAccountDict, toAccount, accountName)
        elif transCode == "EOS":    #   occurs when we have reached the end of transaction summary file
            #   Calls write master accounts file
            writeMaster(masterAccountDict)
            newValidAccountList(masterAccountDict)
        print("\n")
        #for i in masterAccountDict:
        #    print(masterAccountDict[i])

main()
