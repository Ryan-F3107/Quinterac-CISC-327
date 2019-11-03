import tempfile
from importlib import reload
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))



# ---------------------------------------------------- START OF LOGIN ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


def test_r1t1(capsys):
    """Check that you cannot logout before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['logout', 'login', 'atm', 'logout', ' '],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t2(capsys):
    """Check that you cannot create an account before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['createacct', 'login', 'atm', 'logout', 'n'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t3(capsys):
    """Check that you cannot delete an existing account before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['deleteacct', 'login', 'atm', 'logout', 'no'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t4(capsys):
    """Check that you cannot deposit into an account before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['deposit', 'login', 'atm', 'logout', 'no'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t5(capsys):
    """Check that you cannot withdraw from an account before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['withdraw', 'login', 'atm', 'logout', 'NO'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t6(capsys):
    """Check that you cannot transfer between accounts before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['transfer', 'login', 'atm', 'logout', 'No'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t7(capsys):
    """Check that you cannot login before logging out of previous session

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'login', 'atm', 'logout', 'NO'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t8(capsys):
    """Check that you cannot create an account with unprivileged access

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'createacct', 'logout', 'no'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t9(capsys):
    """Check that you cannot delete an account with unprivileged access

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deleteacct', 'logout', 'no'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r1t10(capsys):
    """Check that creating an account works with privileged access

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct',  '1234567', 'accountName1', 'logout', 'no'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['NEW 0000000 000 1234567 accountName1', 'EOS 0000000 000 0000000 ***']
    )


def test_r1t11(capsys):
    """Check that deleting an account works with privileged access

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteacct', '1234567', 'accountName2', 'logout','no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['DEL 0000000 000 1234567 accountName2', 'EOS 0000000 000 0000000 ***']
    )


# ---------------------------------------------------- END OF LOGIN -------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------------- START OF CreateAcct ------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def test_R3T1(capsys):
    """Testing R3T1: The user cannot create an account with an empty account name field

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '2345678', '', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']  # since no transaction (not including
        # login/logout) took place, transaction summary file only consists of EOS
    )


def test_R3T2(capsys):
    """Testing R3T2: The user cannot create an account with an empty account number field

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']  # since no transaction (not including
        # login/logout) took place, transaction summary file only consists of EOS
    )


def test_R3T3(capsys):
    """Testing R3T3: The user cannot create an account with an invalid account number (starting with 0)

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '0123456', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']  # since no transaction (not including
        # login/logout) took place, transaction summary file only consists of EOS
    )


def test_R3T4(capsys):
    """Testing R3T4: The user cannot create an account with an invalid account name (starting/ending with a space)

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '2345678', ' John Doe ', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']  # since no transaction (not including
        # login/logout) took place, transaction summary file only consists of EOS
    )


def test_R3T5(capsys):
    """Testing R3T5: The user cannot create an account with an invalid account name (not enough characters)

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '2345678', 'J', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']  # since no transaction (not including
        # login/logout) took place, transaction summary file only consists of EOS
    )


def test_R3T6(capsys):
    """Testing R3T6: The user cannot create an account with an account number that already exists

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '1234567', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']  # since no transaction (not including
        # login/logout) took place, transaction summary file only consists of EOS
    )


def test_R3T7(capsys):
    """Checking R3T13: User can create an account with a valid account name and number

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '2345678', 'John Doe', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['NEW 0000000 000 2345678 John Doe', 'EOS 0000000 000 0000000 ***']
    )


# ---------------------------------------------------- END OF CreateAcct --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------------- START OF DeleteAcct ------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def test_R4T1(capsys):
    """
    Testing test_R4T1: Can't delete an account with an empty account number field
    Program will give a print statement mentioning that account number field is left empty
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteacct', '', 'logout','no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R4T2(capsys):
    """
    Testing test_R4T2: Can't delete an account with an empty account name field
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deleteacct', '1234567', '', 'logout','no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R4T3(capsys):
    """
    Testing test_R4T3: Can't delete an account with an invalid account number
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteacct', '1234566', 'logout', 'NO'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R4T4(capsys):
    """
    Testing test_R4T4: Can't delete an account with an invalid account name
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteacct', '1234567', 'J', 'logout','no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R4T5(capsys):
    """
    Testing test_R4T5: check that account name and account number is valid
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteAcct', '1234567', 'Johnny Bravo', 'logout','no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['DEL 0000000 000 1234567 Johnny Bravo', 'EOS 0000000 000 0000000 ***']
    )


def test_R4T6(capsys):
    """
    Testing test_R4T6: Can't have empty account fields
    Program will print a statement mentioning that account number field cannot be left empty
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteAcct', '', '', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


# ---------------------------------------------------- END OF DeleteAcct --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

# ---------------------------------------------------- START OF Deposit ---------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def test_R5T1(capsys):
    """
    Testing test_R5T1: Can't deposit to an account with an empty account number field
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '', '1200', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T2(capsys):
    """
    Testing test_R5T2: Can't deposit to an account with an empty amount to deposit field
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1234567', '', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T3(capsys):
    """
    Testing test_R5T3: Checks if the deposit transaction works as it should with the right inputs
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1234567', '13000', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['DEP 1234567 13000 0000000 ***', 'EOS 0000000 000 0000000 ***']
    )


def test_R5T4(capsys):
    """
    Testing test_R5T4: Checks that amount to deposit is valid or not
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1234567', '99999999999', 'logout','no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T5(capsys):
    """
    Testing test_R5T5: Checks that checks that account number is valid or not
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '0234560', '12000', 'logout','n'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T6(capsys):
    """
    Testing test_R5T6: Cannot enter anything non-numeric for the deposit amount
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1234567', 'a-b.c,d?e', 'logout',' '],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T7(capsys):
    """
    Testing test_R5T7: Can't deposit to an account that does not exist
    The program will print a statement mentioning that account does not exist on the terminal
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1847124', 'logout',' '],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T8(capsys):
    """
    Testing test_R5T8: Can't leave the number and deposit field empty
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '', '', 'logout', 'n'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T9(capsys):
    """
    Testing test_R5T9: Can't deposit more than $2000 in atm mode
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1234567', '3000000', 'logout', "no"],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T10(capsys):
    """
    Testing test_R5T10: Can't deposit more than $999999.99 in agent mode
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deposit', '1234567', '999999999', 'logout', 'No'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R5T11(capsys):
    """
    Testing test_R5T11: check if the user can deposit from the agent type login
    :param capsys: object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deposit', '1234567', '500000', 'logout', 'n'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['DEP 1234567 500000 0000000 ***', 'EOS 0000000 000 0000000 ***']
    )


# ---------------------------------------------------- END OF Deposit ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------------- START OF Withdraw --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def test_R6T1(capsys):
    """Testing R6T1: The user cannot withdraw from an invalid account number

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'withdraw', '7654321', 'logout', 'no'],  # no withdrawal amount as program
        # will give an error print statement to user to enter a valid account
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        # session will end once user enters 'logout'
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
        # since no transaction (not including login/logout) took place,
        # transaction summary file only consists of EOS
    )


def test_R6T2(capsys):
    """Testing R6T2: The user cannot withdraw more than $1000 in atm mode

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'withdraw', '1234567', '200000', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
        # since no transaction (not including login/logout) took place,
        # transaction summary file only consists of EOS
    )


def test_R6T3(capsys):
    """Testing R6T3: The user cannot withdraw more than $999,999.99 in agent mode

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'withdraw', '1234567', '200000000', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
        # since no transaction (not including login/logout) took place,
        # transaction summary file only consists of EOS
    )


def test_R6T4(capsys):
    """Testing R6T4: User cannot withdraw with an empty amount field

    Arguments: capsys -- object created by pytest to capture stdout and stderr """
    helper(capsys=capsys,
           terminal_input=['login', 'agent', 'withdraw', '1234567', '', 'logout', 'no'],
           intput_valid_accounts=['1234567'],
           expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                             '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
           expected_output_transactions=['EOS 0000000 000 0000000 ***'])


def test_R6T5(capsys):
    """Testing R6T4: User cannot withdraw with an empty amount field

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'withdraw', '', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R6T6(capsys):
    """Testing R6T6: Check - User should be able to withdraw with the valid account number and amount in atm mode

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'withdraw', '1234567', '2000', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['WDR 0000000 2000 1234567 ***', 'EOS 0000000 000 0000000 ***']
    )


def test_R6T7(capsys):
    """Testing R6T7: Check - User should be able to withdraw with the valid account number and amount in agent mode

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'withdraw', '1234567', '2000', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['WDR 0000000 2000 1234567 ***', 'EOS 0000000 000 0000000 ***']
    )


def test_R6T8(capsys):
    """Testing R6T8: User cannot enter anything non-numeric for the withdrawal amount

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'withdraw', '1234567', 'abcdefgh', 'logout', 'no'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Please enter \'yes\'/\'y\' if you would like to start another session or '
                                          '\'no\'/\'n\' if not: Thank you for using Quinterac, have a nice day!'],
        # need to revisit this
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


# ---------------------------------------------------- END OF Withdraw ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------------- Start of Transfer --------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def test_R7T1(capsys):
    """Testing R7T1: User cannot enter anything non-numeric for account number

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', 'abcdefgh', '2000', 'logout', 'No'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T2(capsys):
    """Testing R7T2: checks that accounts entered are valid

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '12345678', '8', '2000', 'logout', 'No'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T3(capsys):
    """Testing R7T3: checks that outgoing account is not blank

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '', '1234567', '2000', 'logout', ' '],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T4(capsys):
    """Testing R7T4: checks that destination account is not blank

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '', '2000', 'logout', 'No'],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T5(capsys):
    """Testing R7T5: checks that account exists

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '2222222', '1234567', '2000', 'logout', ' '],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T6(capsys):
    """Testing R7T6: checks that destination account exists

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2222222', '2000', 'logout', ' '],
        intput_valid_accounts=['1234567'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T7(capsys):
    """Testing R7T7: checks that amount is not negative

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2345678', '-2000', 'logout', 'No'],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T8(capsys):
    """Testing R7T8: checks that amount is not 0

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2345678', '0', 'logout', ' '],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T9(capsys):
    """Testing R7T9: checks that transfer amount field is not empty

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2345678', '', 'logout', ' '],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T10(capsys):
    """Testing R7T10: checks that transfer amount entered is not non-numeric

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2345678', 'aaa', 'logout', 'No'],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T11(capsys):
    """Testing R7T11: checks that valid account summary file is written

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2345678', '2000', 'logout', ' '],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['XFR 2345678 2000 1234567 ***', 'EOS 0000000 000 0000000 ***']
    )


def test_R7T12(capsys):
    """Testing R7T12: checks that agent can transfer money

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'transfer', '1234567', '2345678', '2000', 'logout', ' '],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['XFR 2345678 2000 1234567 ***', 'EOS 0000000 000 0000000 ***']
    )


def test_R7T13(capsys):
    """Testing R7T13: destination account is the same as the current account

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'transfer', '1234567', '1234567', '2000', 'logout', ' '],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T14(capsys):
    """Additional test
    Testing R7T14: atm can only transfer less then $10000.00
    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'transfer', '1234567', '2345678', '1000001', 'logout', 'No'],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_R7T15(capsys):
    """Additional test
    Testing R7T15: agent can transfer more then $10000.00
    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'transfer', '1234567', '2345678', '2000000', 'logout', 'No'],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['XFR 2345678 2000000 1234567 ***','EOS 0000000 000 0000000 ***']
    )


def test_R7T16(capsys):
    """Additional test: agent cannot transfer more then $999999.99
    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'transfer', '1234567', '2345678', '100000000', 'logout', 'No'],
        intput_valid_accounts=['1234567', '2345678'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )
# ---------------------------------------------------- END OF Transfer ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------------- Start of Logout ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def test_r2t1(capsys):
    """Testing R2T1: Check that you cannot logout before logging in

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['logout', 'login', 'atm', 'logout', 'No'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t2(capsys):
    """Testing R2T1: Check that valid transaction summary file is written after logout

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'no'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t3(capsys):
    """Testing R2T3: cannot logout after logout

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'logout'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t4(capsys):
    """
    Testing R2T4: cannot transfer after logout.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'transfer'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t5(capsys):
    """
    Testing R2T5: cannot withdraw after logout.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'withdraw'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t6(capsys):
    """
    Testing R2T6: cannot deposit after logout.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'deposit'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t7(capsys):
    """
    Testing R2T7: cannot create account after logout.

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'createacct'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t8(capsys):
    """
    Testing R2T8: cannot delete account after logout.


    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'deleteacct'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=['Thank you for using Quinterac, have a nice day!'],
        expected_output_transactions=['EOS 0000000 000 0000000 ***']
    )


def test_r2t9(capsys):
    """
    Testing R2T9: can only login after logout.


    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'logout', 'no', 'login', 'atm', 'logout'],
        intput_valid_accounts=['1234568'],
        expected_tail_of_terminal_output=["Please enter 'yes'/'y' if you would like to start another session or 'no'/'n' if not: Thank you for using Quinterac, have a nice day!"],
        expected_output_transactions=['EOS 0000000 000 0000000 ***', 'EOS 0000000 000 0000000 ***']
    )


# ---------------------------------------------------- End of Logout ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        intput_valid_accounts,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'app.py',
        valid_account_list_file,
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()
    # print out the testing information for debugging
    # the following print content will only display if a
    # test case failed:
    print('std.in:', terminal_input)
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read().splitlines()
        # print out the testing information for debugging
        # the following print content will only display if a
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_output_transactions)

        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
