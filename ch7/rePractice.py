import re
import pyperclip

text = pyperclip.paste()

testRegex = re.compile(r'\w+@\w+.com')

test = testRegex.findall(text)

if test == None:
    print("Nothing")

else:
    print(test)
