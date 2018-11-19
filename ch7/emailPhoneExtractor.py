import re
import pyperclip

def main():
    # Takes from user's clipboard
    text = pyperclip.paste()

    # The regex for phone numbers
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?            # Area code
        (\s|-|\.)?                    # Separator
        (\d{3})                       # First 3 digit
        (\s|-|\.)                     # Separator
        (\d{4})                       # Last 4 digit
        (\s*(ext|x|ext.)\s*\d{2,5})?  # Extension
        )''', re.VERBOSE)

    # The regex for emails
    emailRegex = re.compile(r'\w+\@\w+\.\w+.*?')

    # Finds phones number (and organizes them) and emails from the user's text
    phones = organizeNum(phoneRegex.findall(text))
    emails = emailRegex.findall(text)

    # If there are no numbers, print message
    if phones == None:
        print("No phone numbers found")

    # If there are phone numbers print numbers to the user's screen
    else:
        print("Phone number(s):")

        for number in phones:
            print(number)

    # New line
    print()

    # If there are no emails, print message
    if emails == None:
        print("No emails found")

    # If there are emails print email to user's screen
    else:
        print("Email(s):")

        for email in emails:
            print(email)

# Formats the number to a standard form
def organizeNum(list):
    organized = []

    for number in list:
        # Joins three parts of the number together in xxx-xxx-xxxx format
        temp = '-'.join([number[1], number[3], number[5]])

        # Add extension if exists
        if(number[6] != ''):
            temp += number[6]

        # Add to organized list
        organized.append(temp)

    return organized

if __name__ == "__main__":
    main()
