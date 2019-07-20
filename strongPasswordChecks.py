#strong password checks
import re

#ask the user for the password to check
pwtocheck = input('please enter the password to be checked:')

#Error message to be
Err_mess = ''

#first regex : at least one lower case characters
pw_lc = re.compile(r'([a-z]+)')
        
#second regex : at least one upper case characters
pw_uc = re.compile(r'([A-Z]+)')
    
#third regex: at least one special character
pw_sc = re.compile(r'([\-_\?!@#$%^&\*]+)')

#fourth regex : password must have at least one number
pw_d = re.compile(r'([0-9])+')

#create a list to be given to all() to evaluate if all conditions are met or not
cond_pw = [len(pwtocheck) > 8, pw_lc.search(pwtocheck), pw_uc.search(pwtocheck), pw_sc.search(pwtocheck), pw_d.search(pwtocheck)]


#building an error message
#is the password at least 8 characters
if len(pwtocheck) < 8:
    Err_mess = Err_mess + 'password is too short\n'
    
#first regex is none
if pw_lc.search(pwtocheck) is None:
    Err_mess = Err_mess + 'password needs at least one lower case character\n'
    
#second regex is None
if pw_uc.search(pwtocheck) is None:
    Err_mess = Err_mess + 'password needs at least one upper case character\n'


#third regex is None
if pw_sc.search(pwtocheck) is None:
    Err_mess = Err_mess + 'password needs at least one special character\n'

    
#fourth regex is none
if pw_d.search(pwtocheck) is None:
    Err_mess = Err_mess + 'password needs at least one number\n'
      

if all (cond_pw) is True: 
    print('password is ok')
else:
    print(Err_mess)

