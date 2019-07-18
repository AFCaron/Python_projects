#strong password checks
import re
#ask the user for the password to check
pwtocheck = input('please enter the password to be checked:')

#first regex : lower case characters
pw_lc = re.compile(r'''
    ([a-z]+)
    ''', re.VERBOSE)
    
#second regex : upper case characters
pw_uc = re.compile(r'''
    ([A-Z]+)
    ''', re.VERBOSE)
#third regex: special characters
pw_sc = re.compile(r'''
        ([\-_\?!@#$%^&\*]+)
        ''', re.VERBOSE)


#is the password at least 8 characters
if len(pwtocheck) < 8:
    print('password is too short')
    #pw_state = 'nok'
        #break
        
#first regex is none
if pw_lc.search(pwtocheck) is None:
    print("password doesn't have at least one lower case character")
    #pw_state = 'nok'
        #break
    
#second regex is None
if pw_uc.search(pwtocheck) is None:
    print("password doesn't have at least one upper case character")
    #pw_state = 'nok'
        #break
#third regex is None
if pw_sc.search(pwtocheck) is None:
    print("password doesn't have at least one special character")
    #pw_state = 'nok'
        #break
        
else:
    print('password is ok')

        

print('\nchecks done')
