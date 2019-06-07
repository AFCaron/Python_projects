#Caesar Cypher
#Cyphering/Decyphering class

class Caesar_cypher:
    #class attributes
    #use a dictionary
    a_bet = {'a' : '0','b' : '1','c' : '2','d' : '3','e' : '4','f' : '5','g' : '6','h' : '7','i' : '8','j' : '9','k' : '10','l' : '11','m' : '12','n' : '13','o' : '14','p' : '15','q' : '16','r' : '17','s' : '18','t' : '19','u' : '20','v' : '21','w' : '22','x' : '23','y' : '24','z' : '25'}
    b_bet = {'0' : 'a','1' : 'b','2' : 'c','3' : 'd','4' : 'e','5' : 'f','6' : 'g','7' : 'h','8' : 'i','9' : 'j','10' : 'k','11' : 'l','12' : 'm','13' : 'n','14' : 'o','15' : 'p','16' : 'q','17' : 'r','18' : 's','19' : 't','20' : 'u','21' : 'v','22' : 'w','23' : 'x','24' : 'y','25' : 'z'}
    
    def __init__(self, key, txt):
        self.key = key
        self.txt = txt
        self.l_txt = ''
        
    def convert(self):
        self.l_txt = iter(self.txt)
        
        self.nl_txt =[]
        for letters in self.l_txt:
            self.nl_txt.append(letters)
        
        
        
    def cypher(self):
        self.nb = 0
        self.nl_txt_n = []
        
        for i in self.nl_txt:
            self.nb = int(self.a_bet[i])
            self.new_key = self.nb + self.key
            
            if self.new_key <= len(self.a_bet)-1:
                
                self.nl_txt_n.append(self.b_bet[str(self.new_key)])
                
            elif self.new_key > len(self.a_bet)-1:
                self.nl_txt_n.append(self.b_bet[str(self.new_key-len(self.a_bet))])
                
            self.nb = 0
        self.result = "".join(self.nl_txt_n)
        print(f"the cyphered word is : {self.result}")
        
    def decypher(self):
        self.nb = 0
        self.nl_txt_n = []
        
        for i in self.nl_txt:
            
            self.nb = int(self.a_bet[i])
            
            self.new_key = self.nb - self.key
            
            if self.new_key < 0:
                self.nl_txt_n.append(self.b_bet[str(self.new_key + len(self.b_bet))])
                
            elif self.new_key >= 0:
                self.nl_txt_n.append(self.b_bet[str(self.new_key)])
            self.nb = 0
        self.result = "".join(self.nl_txt_n)
        print(f"the cyphered word is : {self.result}")
        
        
        
        
        
        ##################code######################
choice = input("would you like to cypher or decypher(c/d)?")
key = int(input('please choose a key (int)'))
c_txt = input("input the word you'd like to cypher /decypher ").lower()

c= Caesar_cypher(key, c_txt)
c.convert()
if choice == 'd':
    c.decypher()
elif choice == 'c':
    c.cypher()
        
        
