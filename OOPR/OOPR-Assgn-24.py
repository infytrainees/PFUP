#OOPR-Assgn-24
#Start writing your code here
class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__item_id=None
        self.__price=price
        self.__item_type=item_type
        
        "Logic for Item_Id"
        Apparel.counter+=1
        if item_type=="Silk":
            self.__item_id='S'+str(Apparel.counter)
        elif item_type=="Cotton":
            self.__item_id='C'+str(Apparel.counter)
            
    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def get_item_id(self):
        return self.__item_id

    def get_item_type(self):
        return self.__item_type

    def calculate_price(self):
        self.set_price(1.05*self.get_price())  #adding 5% tax on the price
        



class Cotton (Apparel): 
    def __init__(self,price,discount):
        self.__discount = discount
        super().__init__(price,"Cotton") #setting price of cotton to Apparel
        
    def calculate_price(self):
        super().calculate_price()
        super().set_price(1.05*((1-(self.__discount/100))*super().get_price()))
        
    def get_discount(self):
        return self.__discount




class Silk(Apparel):
    def __init__ (self,price):
        self.__points=None
        super().__init__(price,"Silk") 
        
    def get_points(self):
        return self.__points

    def calculate_price(self):
        super().calculate_price()
        if  super().get_price() > 10000:
            self.__points=10
        else:
            self.__points=3
        super().set_price(1.10*super().get_price())