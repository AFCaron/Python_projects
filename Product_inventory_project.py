#Product Inventory Project
#Create an application which manages an inventory of products.
#Create a product class which has a price, id, and quantity on hand.
#Then create an inventory class which keeps track of various products and can sum up the inventory value.


#product class
class Product(self, price, idn, quantity):
    def__init__(self):
        self.price = price
        self.idn = idn
        self.quantity = quantity
        
        

        
#create a loop to keep the program running
prog = 'run'
while prog = 'run':
    #ask what the user wants to do
    prog = input('what would you like to do? add (a) / remove (r) / sum inventory (s) / quit (q)')
    if prog = 'a':
        #routine for adding a product
            #generating unique ID number each time a product is added
    elif prog = 'r':
        #routine for removing a product
            #selecting the product thru its ID_number
    elif prog = 's':
        #routine for sum of the inventory
    elif prog = 'q':
        #quitting the program
        break

        
#program runs below
#Creating a few 'default' products to populate the system
Pd1 = Product(200, id1, 3)
Pd2 = Product(100, id2, 10)
Pd3 = Product(75, id3, 7)
Pd4 = Product(125, id4, 9)

product_list = [Pd1, Pd2, Pd3, Pd4]
