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
        
    #Creating a few 'default' products to populate the system
    Pd1 = Product(200, 'pump', 3)
    Pd2 = Product(100, 'bearing', 10)
    Pd3 = Product(75, 'hose', 7)
    Pd4 = Product(125, 'washer', 9)

    #Creating a dictionnary linking id mums and product names
    product_Dic = {Pd1.idn : 'Pd1', Pd2.idn : 'Pd2', Pd3.idn : 'Pd3', Pd4.idn : 'Pd4'}    
    
    #add to inventory    
    def add_product(self):
        self.price = price
        self.idn = idn
        self.quantity = quantity
        
        #creating an index for the product key using len(product_Dic)
        index_dic = len(product_Dic)
        #asking for the price per unit, name of the product,quantity
        self.price, self.idn, self.quantity = input("the price per unit, name of the product, quantity").split()
        #creating a new product and adding it to the product dictionary
        npd = Iventory(self.price, self.idn, self.quantity)
        product_Dic.update( {'Pd'+str(len(dic)) : npd.idn} )
        
        
#remove from inventory
#sum of the inventory



#program runs below

        
#create a loop to keep the program running
prog = 'run'
while prog == 'run':
    #ask what the user wants to do
    prog = input('what would you like to do? add (a) / reqmove (r) / sum inventory (s) / quit (q)')
    if prog == 'a':
        print('test_add')
        #routine for adding a product
            #generating unique ID number each time a product is added
    elif prog == 'r':
        print('test_remove')
        #routine for removing a product
            #selecting the product thru its ID_number
    elif prog == 's':
        print('test_remove')
        #routine for sum of the inventory
    elif prog == 'q':
        #quitting the program
        break
        

