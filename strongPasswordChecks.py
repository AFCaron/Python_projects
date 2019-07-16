#strong password checks
#ask the user for the password to check
pwtocheck = input('please enter the password to be checked:')
#state of assword variable
pw_state = 'ok'

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

while pw_state = 'ok':
#is the password at least 8 characters
    if len(pwtocheck) < 8:
        print('password is unsecure : too short')
        break
        
#first regex is none
   if pw_lc.search(pwtocheck) is None:
        print("password doesn't have at least one lower case character")
        break
    
#second regex : upper case characters
    elif pw_uc.search(pwtocheck) is None:
        print("password doesn't have at least one upper case character")
        break
#third regex: special characters
    elif pw_sc.search(pwtocheck) is None:
        print("password doesn't have at least one special character")
        break
        
#to be continued
