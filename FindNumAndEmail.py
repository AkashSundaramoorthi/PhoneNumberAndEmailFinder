#! python3
import re, pyperclip



phone = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000
(((\d\d\d)|(\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d)
''',re.VERBOSE)

email = re.compile(r'''
#some.some@some.com

[a-zA-z0-9.+_]+
@
[a-zA-z0-9.+_]+
''',re.VERBOSE)
text = pyperclip.paste()
phonef = phone.findall(text)
emailf = email.findall(text)

allnum = []

for i in phonef:
    allnum.append(i[0])

numberExtracted = '\n'.join(allnum)
emailExtracted = '\n'.join(emailf)

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

