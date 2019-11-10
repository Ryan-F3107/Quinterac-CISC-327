"""
CISC 327 - Assignment 4
Authors:
        Anna Chulukov, 17avc2@queensu.ca, 20082947
        Faranak Sharifi, 17fsb@queensu.ca, 20068900
        Marwan ElKhodary, m.elkhodary@queensu.ca, 20022212
        Ryan Fernandes, 17rf@queensu.ca, 20067569
Due:
"""

import sys

def readTransFile():
    merged_TSF = sys.argv[1]
    with open(merged_TSF) as transactionFile:
        transactionList = transactionFile.read().splitlines()

    return transactionList  # returns transactions as individual strings in a list

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
            try:
                a=int(accountNum)
                b=int(accountBalance)
            except ValueError:
                exit("Fatal ERROR")
            masterAccountDict[accountNum] = [accountBalance, accountName]

    return masterAccountDict   # returns the accounts as objects in a list


def deposit(masterAccountDict, accountNum, amount):
    # see how much money they have
    moneyHave = masterAccountDict[accountNum][0]  # check if this should be toAccount or accountNum

    # add it to the amount they want to deposit
    moneyHave = int(moneyHave) + int(amount)

    # store new amount of money back into the dictionary
    masterAccountDict[accountNum][0] = str(moneyHave)
    dollars = str(int(amount) / 100)
    print(dollars+" was deposited into "+accountNum)
    return masterAccountDict

def withdraw(masterAccountDict, accountNum, amount):
    # see how much money they have
    moneyHave = masterAccountDict[accountNum][0]  # check if this should be toAccount or accountNum
    # subtract it by the amount they want to withdraw
    moneyHave = int(moneyHave) - int(amount)
    if moneyHave < 0:
        print("Do not have enough funds to withdraw!")
        return masterAccountDict
    # store new amount of money back into the dictionary
    masterAccountDict[accountNum][0] = str(moneyHave)
    dollars = str(int(amount) / 100)
    print(dollars + " was whithdrawn from " + accountNum)
    return masterAccountDict

def transfer(masterAccountDict, destAccount, fromAccount, amount):
    # get money in first account
    moneyHave = masterAccountDict[fromAccount][0]

    # subtract how much they have to how much they want to transfer
    moneyHave = int(moneyHave) - int(amount)
    if moneyHave < 0:
        print("Do not have enough funds to transfer!")
        return masterAccountDict
    # store new amount of money back into the dictionary
    masterAccountDict[fromAccount][0] = str(moneyHave)
    # add to money they have to how much they were transferred
    moneyHave2 = int(masterAccountDict[destAccount][0]) + int(amount)

    # store new amount of money back into the dictionary
    masterAccountDict[destAccount][0]  = str(moneyHave2)
    dollars=str(int(amount)/100)
    print("$"+dollars + " was transfered to " + destAccount)
    return masterAccountDict

"""
Constraints:
- each line is at most 47 characters (plus newline)
- items are separated by exactly one space
- account numbers, monetary amounts, and account names are as described
 for the transaction summary file above
- the Master Accounts File must always be kept in descending order by
 account number
 """
def writeMaster():
    b=1
    return


def main():
    #read dictionary that has account number, account balance and account name
    masterAccountDict = readMaster()

    #read transactions in a list
    transactionList = readTransFile()

    for x in transactionList:  #goes through a list of transactions
        eachTransaction = x.split()
        transCode = eachTransaction[0]
        accountNum = eachTransaction[1] #also destAccount
        if transCode!="NEW" and transCode!="EOS":
            try:
                masterAccountDict[accountNum]
            except KeyError:
                print("There is no such account!")
                exit("Fatal ERROR")
        amount = eachTransaction[2]
        fromAccount = eachTransaction[3]
        accountName = eachTransaction[4]

        if transCode == "DEP":
            print(masterAccountDict[accountNum])
            masterAccountDict=deposit(masterAccountDict, accountNum, amount)
            print(masterAccountDict[accountNum])
        elif transCode == "WDR":
            masterAccountDict=withdraw(masterAccountDict, accountNum, amount)
        elif transCode == "XFR":
            masterAccountDict=transfer(masterAccountDict, accountNum, fromAccount, amount)
        elif transCode == "NEW":
            if accountNum in masterAccountDict:
                print("Please enter new account number, this one is taken!")
            else:
                #it says no transactions should be accepted when making a new account, so I just set the amount to 0000
                masterAccountDict[accountNum] = ["0000", accountName]
                print(accountNum+" was created")
        elif transCode == "DEL":
            accountNameMaster = masterAccountDict[accountNum][1]
            accountBalance = masterAccountDict[accountNum][0]
            if accountNameMaster != accountName:
                print("names do not match!")
            elif accountBalance != 0:
                print("\n\nRyan and Marwan do you think we need this??")
                print("\naccount balance is not zero, it has to be zero!")
            else:
                print("deleting account")
                del masterAccountDict[accountNum]
                print(accountNum + " was deleted")
        elif transCode == "EOS":
            pass
    #for i in masterAccountDict:
    #    print(masterAccountDict[i])


main()
