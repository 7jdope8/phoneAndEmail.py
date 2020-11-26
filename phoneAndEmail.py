#PROJECT (Phone number and Email Address Exctractor)

# What does the program need to do? 

# - Get the text off the clipboard 
# - Find all phone numbers and email addresses in the text. 
# - Paste them onto the clipboard. 

# How might this work in code? 

# - Use the pyperclip module to copy and paste strings. 
# - Create two regexes, one for matching phone numbers and the other for matching email addreses. 
# - Find all matches, not just the first match, of both regexes. 
# - Neatly format the matched strings into a single string to paste. 
# - Display some kind of message if no matches were found in the text. 

# Create phone regex 

import pyperclip, re

phoneRegex = re.compile(r'''(

    (\d{3}|\(d{3}\))?           # area code (optional because it has a question mark) and | becuase an option of the both 
    (\s|-|\.)?                  # separator (either a space or a hyphen signaled with | )
    (\d{3})                     # First 3 Digits signaled by \digit and {3} times. 
    (\s|-|\.)                   # Separator (either a space or a hyphen signaled with | )     
    (\d{4})                     # Last 4 digits signaled by \digit and {4} times. 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?          # extension from {2 to 5 digits}
    )''', re.VERBOSE)                       # re.VERBOSE adds comments to the right to make it beautiful. 

# TODO: Create email regex 
emailRegex = re.compile(r'''(

    [a-zA-Z0-9._%+-]+       # username 
    @                       # @ symbol 
    [a-zA-Z0-9.-]+          # domain name 
    (\.[a-zA-Z]{2,4})       # dot-something 
    )''', re.VERBOSE)       

#Find matches in clipboard text. 

text = str(pyperclip.paste())           # Paste from board
matches = []                            # Start off with an empty list 
for groups in phoneRegex.findall(text): # find every phone number 
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # area code, first three digits, last four digits, and extension 
    if groups[8] != '':                 # if there's still another group to add 
        phoneNum += ' x' + groups[8]    # add it after an x
    matches.append(phoneNum)            # append the new phone numbers to the previously empty list. 
for groups in emailRegex.findall(text): # very simple, just find every email address
    matches.append(groups[0])           # And then append it in a list

# Copy results to the clipboard. 

if len(matches) > 0: 
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else: 
    print('No phone numbers or email addresses found')