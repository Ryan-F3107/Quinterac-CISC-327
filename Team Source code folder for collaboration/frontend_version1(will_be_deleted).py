import sys

def withdraw(accountNumber, amountCents):

def main():
    accountsFileDir = sys.argv[1]
    with open(accountsFileDir) as accountsFile:
        accountsList = accountsFile.read().splitlines()
    command = input()
    if command == "withdraw":
        accountNumberInput = input()
        amountCentsInput = input()
        withdraw(accountNumberInput, amountCentsInput)
main()