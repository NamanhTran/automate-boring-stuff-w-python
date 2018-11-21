# Multiclipboard

**ONLY WORKS IN LINUX**

This program will save each piece of clipboard text under a keyword. For example, when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam. This text can later be loaded to the clipboard again by running py mcb.pyw spam. And if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

## COMMANDS

    - python mcb.pyw save *keyword*
        - will save what ever is on your clipboard to that keyword

    - python mcb.pyw *keyword*
        - will send the value of the keyword to your clipboard

    - python mcb.pyw list
        - will paste to your clipboard all the keyword stored in the program

    - python mcb.pyw delete *keyword*
        - will delete the keyword and it's value in the program

    - python mcb.pyw delete
        - will wipe all data stored in the program
