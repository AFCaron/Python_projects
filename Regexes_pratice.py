#Regexes to recover phone numbers and e-mail adresses from the clipboard
#get the content from the clipboard
import re
from tkinter import Tk
sourceTxt = Tk().clipboard_get()

#function to remove duplicates in the result lists
def remove_duplicate(func):
    remove_duplicate.nfunc = []
    lfunc = len(func)
    for i in range(len(func)-1):
        for j in range(len(func)-1):
            if len(func) > 1 and i == j and func[i] == func[j] and not func[i] in remove_duplicate.nfunc:
                remove_duplicate.nfunc.append(func[i])
    return  remove_duplicate.nfunc


#phone number finder
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.)? # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

print(phoneRegex.findall(sourceTxt))
mo1 = remove_duplicate(phoneRegex.findall(sourceTxt))



#e-mail finder
mailRegex = re.compile(r'''(
    [a-zA-Z0-9-\._]+
    @
    [a-zA-Z0-9-\._]+
    .
    [a-z]+
    )''', re.VERBOSE)
print(mailRegex.findall(sourceTxt))
mo2 = remove_duplicate(mailRegex.findall(sourceTxt))
print(mo2)

#getting only the complete number match 
if len(mo1) > 0:
    print(f'{len(mo1)} phone number(s) were found :')
    for numbers_ph in range(len(mo1)):
        print(mo1[numbers_ph][0])
        
        
else:
    print('no phone numbers were found')


if len(mo2) > 0:
    print(f'{len(mo2)} email addresse(s) were found :')
    for numbers_em in range(len(mo2)):
        print(mo2[numbers_em])
else:
    print('no e-mail adresses were found')
