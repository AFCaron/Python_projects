#Regexes to recover phone numbers and e-mail adresses from the clipboard
#get the content from the clipboard
from Tkinter import Tk
sourceTxt = Tk().clipboard_get()

#phone number finder
phoneRegex1 = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)



#e-mail finder
mailRegex = re.compile(r'''(
    [a-z0-9]+
    @
    [a-z]+
    .
    [a-z]+
    )''', re.VERBOSE)
mo2 = mailRegex.findall('monvier13@blabla.com, test@gmail.com, tarace@osti.qc')
print(f'{len(mo2)} email addresses were found :')
for numbers in range(len(mo2)):
    
    print(mo2[numbers])
