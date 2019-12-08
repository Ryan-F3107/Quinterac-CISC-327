import glob  # used to retrieve all transaction summary files in a list from the directory the program is in
import functools  # used to flatten a 2d array
import operator  # used to flatten a 2d array
import os


def readFiles():
    transactionCodesNotFlat = []
    for f in glob.glob("your_transaction_summary_*"):  # iterates through all files within the directory that start
        # with 'your_transaction_summary_'
        file = open(str(f), "r")
        transactionCodesNotFlat.append(file.read().splitlines())  # array of transaction codes is initially a 2d array
        file.close()
        os.remove(f)
        # due to this line
    transactionCodes = functools.reduce(operator.iconcat, transactionCodesNotFlat, [])  # flattens 2d array into a 1d
    # array

    return transactionCodes


def mergeTransactionSummaryFiles(transactionCodes):
    with open("merged_transaction_summary.txt", "w") as file:
        for transaction in transactionCodes:
            file.write(transaction + "\n")


def main():
    transactionsList = readFiles()
    mergeTransactionSummaryFiles(transactionsList)


main()
