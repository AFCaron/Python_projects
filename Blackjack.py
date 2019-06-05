import random
game = 'Y'
a = Account(int(input("select the amount to put on your account ")))
game = input("shall we start a game of black jack? (Y/N)").upper()
while game == 'Y':
    #game = input("shall we start a game of black jack? (Y/N)").upper()
    if game == 'N':
        break

    class Deck():

            #class object attributes
        deck_list = ['Ace of spades', 'Ace of hearts','Ace of diamonds', 'Ace of cubs', '2 of spades', '2 of hearts','2 of diamonds', '2 of cubs', '3 of spades', '3 of hearts','3 of diamonds', '3 of cubs', '4 of spades', '4 of hearts','4 of diamonds', '4 of cubs', '5 of spades', '5 of hearts','5 of diamonds', '5 of cubs', '6 of spades', '6 of hearts','6 of diamonds', '6 of cubs', '7 of spades', '7 of hearts','7 of diamonds', '7 of cubs', '8 of spades', '8 of hearts','8 of diamonds', '8 of cubs', '9 of spades', '9 of hearts','9 of diamonds', '9 of cubs', '10 of spades', '10 of hearts','10 of diamonds', '10 of cubs', 'jack of spades', 'jack of hearts','jack of diamonds', 'jack of cubs', 'queen of spades', 'queen of hearts','queen of diamonds', 'queen of cubs', 'king of spades', 'king of hearts','king of diamonds', 'king of cubs']
        #rando_list = random.choices(deck_list, k=5) # we pick 5 cards in case the player needs a third card
        rando_list = random.sample(deck_list, k=5) # we pick 5 cards in case the player needs a third card


        def __init__(self):
            print('drawing cards')        

        def card_dealing_player(self):
            self.player_cards = [Deck.rando_list[0], Deck.rando_list[2], Deck.rando_list[4]]
            self.dealer_cards = [Deck.rando_list[1], Deck.rando_list[3]]

        def Hit(self):
            self.player_cards = d.player_cards
            print(f"your deck is {d.player_cards}\nthe dealer deck is {d.dealer_cards}\n")

        def Stand(self):
            self.player_cards = d.player_cards[0:2]
            print(f"your deck is {d.player_cards}\nthe dealer deck is {d.dealer_cards}\n")

        def Evaluate_player(self):
            self.player_score = 0
            self.dealer_score = 0

            for i in range(len(d.player_cards)):

                if d.player_cards[i][0] in '23456789':
                    self.player_score = self.player_score + int(d.player_cards[i][0])
                elif d.player_cards[i][0] == 'A':
                    self.player_score = self.player_score + int(input("would you like the Ace to be worth 1 or 10? "))
                elif d.player_cards[i][0:2] == '10':
                    self.player_score = self.player_score + 10
                else:
                    self.player_score = self.player_score + 10

            print(f"your score is {self.player_score}")

            for i in range(len(d.dealer_cards)):

                if d.dealer_cards[i][0] in '23456789':
                    self.dealer_score = self.dealer_score + int(d.dealer_cards[i][0])
                elif d.dealer_cards[i][0] == 'A':
                    self.dealer_score = self.dealer_score + int(input("would you like the Ace to be worth 1 or 10? "))
                elif d.dealer_cards[i][0:2] == '10':
                    self.dealer_score = self.dealer_score + 10
                else:
                    self.dealer_score = self.dealer_score + 10

            print(f"dealer's score is {self.dealer_score}")

    class Account():
        def __init__(self, balance):
            self.balance = balance

        def Bet(self, amount):
            self.amount = amount

        def deposit(self, amount):
            self.balance = self.balance + amount
            print(f"yout new balance is {a.balance}")

        def withdraw(self, amount):
            if self.balance - amount <= 0:
                self.balance = self.balance - amount
                print("you ran out of money")
                game = 'N'
            elif self.balance - amount > 0:
                self.balance = self.balance - amount
                print(f"yout new balance is {a.balance}")

    
    
    
   

    #a = Account(int(input("select the amount to put on your account ")))

            
         
    d = Deck()
    d.card_dealing_player()
    print(f"your deck is {d.player_cards[0:2]}") #the player deck is displayed
    print(f"the dealer deck is {d.dealer_cards[0]}\n") #the dealer deck is displayed
    
    a.Bet(int(input("how much would you like to bet? \n")))
    #prompt to ask the player to hit or stand
    H_or_S = ''
    
    while H_or_S != 'hit' and H_or_S != 'stand':
          H_or_S = input("Would you like to hit or stand? \n").lower()
    
    #run hit or stand functions depending on player choice
    if H_or_S == 'hit':
          d.Hit()
    elif H_or_S == 'stand':
          d.Stand()
            
    d.Evaluate_player() #counting the scores
    
    #compare the scores
    if d.dealer_score and d.player_score < 22:
        winner = max(d.dealer_score, d.player_score)
        if d.dealer_score == winner:
            print("dealer wins\n")
            a.withdraw(a.amount)
            
        elif d.player_score == winner:
            print("player wins\n")
            a.deposit(a.amount)
            
    elif d.dealer_score > 21:
        print("dealer looses\n")
    elif d.player_score > 21:
        print("player looses\n")
        a.withdraw(a.amount)
    
    
   
    game = input("shall we play another game of black jack? (Y/N)").upper()
