import random


class password:
    
    abet = 'abcdefghijklmnopqrstuvwxyz'
    spec_bet = '!@#$%^&*()_+?'
    
    
    def __init__(self, nb_bit):
        self.nb_bit = nb_bit
        
    def pw_gen(self):
        self.charac_type = 0 #variable to be used to decide the type of character
        self.charac_pos = 0
        self.old_type = random.randint(0,3) # old_type will be used to make sure there won't be 2 same characters on after the other
        self.pw =''
        for i in range(0, self.nb_bit):
            while self.charac_type == self.old_type:
                
                self.charac_type = random.randint(0,3) #randomly selecting the type of character
                
            
            if self.charac_type == 0: # lower case character
                self.charac_pos = random.randint(0,25) # picking a random number to choose a letter in the alphabet
                self.pw = self.pw + self.abet[self.charac_pos]
                
            elif self.charac_type == 1: # lower case character
                self.charac_pos = random.randint(0,25) # picking a random number to choose a letter in the alphabet
                self.pw = self.pw + self.abet[self.charac_pos].upper()
                
            elif self.charac_type == 2: # lower case character
                self.pw = self.pw + str(random.randint(0, 9))
            
            elif self.charac_type == 3: #special characters
                self.charac_pos = random.randint(0,12) # picking a random number to choose a sepcial character
                self.pw = self.pw + self.spec_bet[self.charac_pos]
                
            self.old_type = self.charac_type
            
        print(f'your password is {self.pw}')
              
              
while True:
    bits = int(input('what should the bit length of your password be? '))
              
    if bits >= 8:
        p = password(bits)
        p.pw_gen()
        break
    elif bits < 8:
        print('for security reasons the number of bits cannot be inferior to 8')
