import sys
import pyperclip


def main():

    if len(sys.argv) != 2:

        print("Usage: python3 pw.py [password]")
        sys.exit()
        
    else:
        # hardcoded accounts
        accountBank = {"Namanh" : "123"}

        # set account name
        account = sys.argv[1]

        # create menu for user to send unput
        operation = menu()

        # sets password for the account
        if operation == 1:

            # set password for the account given
            setPwd(account, accountBank)

        # gets password for the account
        else:

            # get password for the account given
            getPwd(account, accountBank)

def getPwd(account, bank):
    
    if account not in bank:
        print("Account not found in the database.")
        return

    pyperclip.copy(bank[account]);
    print("Copied to your clipboard!")
   
def setPwd(account, bank):

    print("Set password for this account")
    
    bank[account] = input()

def menu():
    choice = 0;
    while choice != 1 and choice != 2:
        print("1) Set a password for this account\n")
        print("2) Get a password for this account\n")
        choice = int(input())

    return choice

if __name__ == "__main__":
    main()
