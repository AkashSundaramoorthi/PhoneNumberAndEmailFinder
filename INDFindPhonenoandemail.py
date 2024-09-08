#! python3
import re, pyperclip

#Indian Phone Number Format
phone = re.compile(r'''
#+91 12345 67890, +91 1234567890, 1234567890,12345 67890,12345-67890
((\+91\s?)?
(\d{5})
(\s|-)?
(\d{5}))
''',re.VERBOSE)

#Email format
email = re.compile(r'''
#some.some@some.com

[a-zA-z0-9.+_]+
@
[a-zA-z0-9.+_]+
''',re.VERBOSE)

#Paste the text from clipboard
text = pyperclip.paste()

#Find all the phone number and emails from clipboard
phonef = phone.findall(text)
emailf = email.findall(text)

allnum = []

for i in phonef:
    allnum.append(i[0])

numberExtracted = '\n'.join(allnum)
emailExtracted = '\n'.join(emailf)

#Copy extracted phone number and email to clipboard
if len(allnum) == 0 and len(emailf) == 0:
    print("There are no numbers and emails in the text that you have copied.\n")
elif len(allnum)==0:
    print("There are no numbers in the text that you have copied.\n")
    pyperclip.copy(emailExtracted)
    print("All extracted email has been copied to clipboard.\n")
elif len(emailf)==0:
    print("There are no emails in the text that you have copied.\n")
    pyperclip.copy(numberExtracted)
    print("All extracted numbers has been copied to clipboard.\n")
else:
    print("All extracted numbers copied to clipboard.\n")
    pyperclip.copy(numberExtracted)
    print("Enter yes if you want to copy email also.\n")
    ans = input().lower()
    if ans == "yes" or ans =="y":
        pyperclip.copy(emailExtracted)
        print("All extracted email has been copied to clipboard.\n")
        

