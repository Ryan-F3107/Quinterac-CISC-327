# CISC 327 A2, main Class
class Login:
    def __init__(self, accountsList, session):
        print("init")
        self.accountsList = accountsList
        self.session = session


class Createacct:
    def __init__(self, accountNum, accountName):
        self.name=accountName
        self.num=accountNum
        print("create")

    def print(self):
        print("Account Name: "+self.name+" \nAccount Number"+self.num)

def createAcct(accountsList):
    accountNum=input("Please enter an account number")
    accountName = input("Please enter an account name")
    try:
        accountNum = int(accountNum)
    except ValueError:
        print("you did not enter an integer")
    finally:
        if accountNum in accountsList:
            print("Account is already created")
            return None, accountsList
        # check validity of info later
        anAccount=Createacct(accountNum, accountName)
        accountsList.append(accountNum)
        return anAccount, accountsList


def deleteAcct(accountsList):
    accountNum=input("Please enter an account number to delete: ")
    try:
        accountNum=int(accountNum)
    except ValueError:
        print("you did not enter an integer")
        return accountsList
    finally:
        if accountNum not in accountsList:
            print("Account does not exist")
            return accountsList
        accountsList.remove(accountNum)
        print("you have sucessfully deleted ", accountNum)
        return accountsList

def main():
    ##
    ##USE SWITCH SYSTEMS
    ##
    # filler for now
    please = "Please enter transaction: "
    accountsList = [3213214, 1234567, 78910111]
    priviledged = ['create', 'delete']
    day = True
    while day:
        print("\n\nThis is a new session")
        p =input(please)
        if p == 'login':
            #put the login stuff in a login function that created object
            session = input("Please enter type of session (atm or agent)")
            login_1 = Login(accountsList, session)
            transaction = input(please)
            if transaction == 'login':
                print("Need to logout before login")
                transaction = input(please)
            else:
                while transaction != 'logout':
                    if transaction in priviledged:
                        #if creating or deleting account check if its an agent
                        if login_1.session == 'agent':
                            print("Permission Confirmed")
                            if transaction == 'createacct':
                                crObj, accountsList = createAcct(accountsList)
                                print("create")
                                transaction = input(please)
                            elif transaction == "deleteacct":
                                print("delete")
                                accountsList = deleteAcct(accountsList)
                                transaction = input(please)
                        else:
                            print("Do not have permission")
                            transaction = input(please)
                            # keep adding code

                    else: #transaction not priviledged
                        if transaction=="withdraw":
                            print("#withdraw")
                            #withdraw
                            transaction = input(please)
                        elif transaction=="transfer":
                            print("transfer")
                            #transfer
                            transaction = input(please)
                        elif transaction=="deposit":
                            print("deposit")
                            transaction = input(please)
                        else:
                            print("transaction not recognized")
                            transaction = input(please)
#delete account from valid accoutns file
        else:
            print("Need to login first")
main()
