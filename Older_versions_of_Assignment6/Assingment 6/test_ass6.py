import tempfile
from importlib import reload
import os
import io
import sys
import app as app
import backend as backend

path = os.path.dirname(os.path.abspath(__file__))


filenames = []
# ---------------------------------------------------- START OF LOGIN ------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


def test_front_end_createacct(capsys):
    """Check that you can create an account using front end

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'createacct', '1111111', 'heller', 'no'],
        input_valid_accounts=['1234567']
    )
    file="T1"
    makeFile(file)

def test_front_end_delAcct(capsys):
    """Check that you can delete an account using front end

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'agent', 'deleteacct', '1111111', 'heller', 'no'],
        input_valid_accounts=['1234567', '1111111']
    )
    file="T2"
    makeFile(file)

def test_front_end_deposit(capsys):
    """Check that you can delete an account using front end

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=['login', 'atm', 'deposit', '1234567', '13000', 'logout','no'],
        input_valid_accounts=['1234567', '1111111']
    )
    file = "T3"
    makeFile(file)


def test_backend():
    mergeAllFiles()
    backend.main()


# ---------------------------------------------------- End of Login ----------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

def makeFile(s):
    i = 0
    for x in app.transactionCodes:
        f = open(s + '.txt', "w")
        filenames.append(s + '.txt')
        i = i + 1
        f.write(x+"\n")
        f.write("EOS 0000000 000 0000000 ***")
        f.close()


def mergeAllFiles():

    with open('merged_transaction_summary.txt', "w") as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read() + "\n")




def helper(
        capsys,
        terminal_input,
        input_valid_accounts

):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        input_valid_accounts -- list of valid accounts in the valid_account_list_file
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
        wf.write('\n'.join(input_valid_accounts))

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
    # print('std.in:', terminal_input)
    # print('valid accounts:', input_valid_accounts)
    # print('terminal output:', out_lines)
    # print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    # for i in range(1, len(expected_tail_of_terminal_output)+1):
    #     index = i * -1
    #     assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    # with open(transaction_summary_file, 'r') as of:
    #     content = of.read().splitlines()
    #     # print out the testing information for debugging
    #     # the following print content will only display if a
    #     # test case failed:
    #     print('output transactions:', content)
    #     print('output transactions (expected):', expected_output_transactions)
    #
    #     for ind in range(len(content)):
    #         assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)

