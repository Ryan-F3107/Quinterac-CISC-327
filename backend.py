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


        for y in masterList:
            eachAccount = y.split()
            accountNum = eachAccount[0]
            accountBalance = eachAccount[1]
            accountName = eachAccount[2]

            masterAccountDict[accountNum] = [accountBalance, accountName]

    return masterAccountDict   # returns the accounts as objects in a list

def main():
    #read dictionary that has account number, account balance and account name
    masterAccountDict = readMaster()

    #read transactions in a list
    transactionList = readTransFile()

    for x in transactionList:  #goes through a list of transactions
        eachTransaction = x.split()
        transCode = eachTransaction[0]
        accountNum = eachTransaction[1]
        amount = eachTransaction[2]
        toAccount = eachTransaction[3]
        accountName = eachTransaction[4]

        #do things related to deposit
        if transCode == "DEP":
            store = masterAccountDict[toAccount]  #check if this should be toAccount or accountNum
            #see how much money they have
            moneyHave = store[0]
            #add it to the amount they want to deposit
            moneyHave = int(moneyHave) + int(amount)

            #not sure if we need this since they are depositing
            if moneyHave < 0:
                print("Do not have enough funds!")

            # store new amount of money back into the dictionary
            store[0] = str(moneyHave)

        if transCode == "WDR":
            store = masterAccountDict[toAccount]  # check if this should be toAccount or accountNum
            # see how much money they have
            moneyHave = store[0]
            # subtract it by the amount they want to withdraw
            moneyHave = int(moneyHave) - int(amount)

            if moneyHave < 0:
                print("Do not have enough funds!")

            # store new amount of money back into the dictionary
            store[0] = str(moneyHave)

        if transCode == "XFR":
            store = masterAccountDict[accountNum]
            # get money in first account
            moneyHave = store[0]
            #subtract how much they have to how much they want to transfer
            moneyHave = int(moneyHave) - int(amount)

            if moneyHave < 0:
                print("Do not have enough funds!")

            # store new amount of money back into the dictionary
            store[0] = str(moneyHave)

            # get money in second account
            store2 = masterAccountDict[toAccount]
            moneyHave2 = store2[0]
            #add to money they have to how much they transferred
            moneyHave2 = int(moneyHave2) + int(amount)

            if moneyHave2 < 0:
                print("Do not have enough funds!")


            # store new amount of money back into the dictionary
            store[0] = str(moneyHave2)

        if transCode == "NEW":
            if accountNum in masterAccountDict:
                print("Please enter new account number, this one is taken!")
            else:
                #it says no transactions should be accepted when making a new account, so I just set the amount to 0000
                masterAccountDict[accountNum] = ["0000", accountName]
        if transCode == "DEL":
            store = masterAccountDict[accountNum]
            accountNameMaster = store[1]
            accountBalance = store[0]

            if accountNameMaster != accountName:
                print("names do not match!")
            elif accountBalance != 0:
                print("account balance is not zero, it has to be zero!")
            else:
                del masterAccountDict[accountNum]



        if transCode == "EOS":
            pass




main()
