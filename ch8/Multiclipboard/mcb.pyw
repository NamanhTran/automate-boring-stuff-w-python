import sys
import os
import pyperclip
import shelve

def main():
    # Saves clipboard to keyword given
    if len(sys.argv) == 3 and sys.argv[1] == 'save':
        # Opens shelve file
        shelfFile = shelve.open('mydata')

        # Assign value to key in shelve dicitonary
        shelfFile[sys.argv[2]] = pyperclip.paste()

    # Sends value to clipboard
    elif len(sys.argv) == 2 and sys.argv[1] == 'list':
        # Opens shelve file
        shelfFile = shelve.open('mydata')

        # Initalize content string
        content = ''

        # Add keys from shelve file to string
        for keys in shelfFile:
            content += keys + ' '

        # Copy to the clipboard
        pyperclip.copy(content)

    # Delete certain element in the shelve dicitonary
    elif len(sys.argv) == 3 and sys.argv[1] == 'delete':
        # Opens shelve file
        shelfFile = shelve.open('mydata')

        # Delete element from shelve dictionary
        del shelfFile[sys.argv[2]]

    # Delete the shelf file
    elif sys.argv[1] == 'delete':
        os.remove('./mydata')

    # Get the value from the shelve dictionary
    elif len(sys.argv) == 2:
        # Opens shelve file
        shelfFile = shelve.open('mydata')
        
        # If not in shelf then give error message
        if sys.argv[1] not in list(shelfFile.keys()):
            print('Data for that keyword does not exist')
        
        # Copy value to clipboard
        pyperclip.copy(shelfFile[sys.argv[1]])

    # Print error message if user did not put any arguments
    else:
        print('Usage: python mcb.py [save/delete/list] [keyword]')

if __name__ == "__main__":
    main()