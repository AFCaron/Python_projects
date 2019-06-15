#Product Inventory Project
#Create an application which manages an inventory of products.
#Create a product class which has a price, id, and quantity on hand.
#Then create an inventory class which keeps track of various products and can sum up the inventory value.


#product class
class Product:
    def __init__(self, price, idn, quantity):
        self.price = price
        self.idn = idn
        self.quantity = quantity
        
#inventory class
class Inventory(Product):
    def __init__(self, price, idn, quantity):
        Product.__init__(self, price, idn, quantity)
        
    
    
    #add to inventory    
    def add_product(self):
        self.price = price
        self.idn = idn
        self.quantity = quantity
        
        #creating an index for the product key using len(product_Dic)
        index_dic = len(product_Dic) + 1
        #updating the product dictionary
        product_Dic.update( {'Pd'+str(index_dic) : [self.idn, self.price, self.quantity]} )
        
        

#program runs below
#Creating a few 'default' products to populate the system
Pd1 = Product(200, 'pump', 3)
Pd2 = Product(100, 'bearing', 10)
Pd3 = Product(75, 'hose', 7)
Pd4 = Product(125, 'washer', 9)

#Creating a dictionnary linking id mums and product names
#product_Dic = {Pd1.idn : 'Pd1', Pd2.idn : 'Pd2', Pd3.idn : 'Pd3', Pd4.idn : 'Pd4'}
product_Dic = {
                'Pd1' : [Pd1.idn, Pd1.price, Pd1.quantity],
                'Pd2' : [Pd2.idn, Pd2.price, Pd2.quantity],
                'Pd3' : [Pd3.idn, Pd3.price, Pd3.quantity],
                'Pd4' : [Pd4.idn, Pd4.price, Pd4.quantity]
              }
        
#create a loop to keep the program running
while True:
    #ask what the user wants to do
    prog = input('what would you like to do? add (a) / remove (r) / sum inventory (s) / quit (q)\n')
    if prog == 'a':
        
        #routine for adding a product
        #asking for the price per unit, name of the product,quantity
        price, idn, quantity = input("the price per unit, name of the product, quantity").split()
        pdct = Inventory(price, idn, quantity)
        pdct.add_product()
        
    elif prog == 'r':
        #routine for removing a product
        to_del = input('Enter Product ID to be deleted\n')
        #error handling in case a non existent ref is entered
        try:
            del product_Dic[to_del]
            print(f'product {to_del} was removed from the database\n')
        except:
            print("couldn't find the product you are trying to delete\n")
        
    elif prog == 's':
        #routine for sum of the inventory
        tot_val = 0
        print('[product name, price per unit, quantity]')
        for keys in product_Dic:
            tot_val += (int(product_Dic[keys][1]))*(int(product_Dic[keys][2]))
            print(product_Dic[keys])
        print(f"\nthe total value of the inventory is ${tot_val}")
    elif prog == 'q':
        #quitting the program
        break

        

