#OOPR-Assgn-25
#Start writing your code here

class FruitInfo:
    __fruit_name_list=["Apple","Guava","Orange","Grape","Sweet lime"] 
    __fruit_price_list=[200,80,70,110,60]
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            indx=FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[indx]
        else:
            return -1
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
    
class Purchase:
    __counter=101
    def __init__(self,customer,fruit_name,quantity):
        
        self.__customer = customer
        self.__fruit_name= fruit_name
        self.__quantity = quantity
        self.__purchase_id = 'P'+str(Purchase.__counter)
        Purchase.__counter+=1

    def calculate_price(self):
        if FruitInfo.get_fruit_price(self.__fruit_name) != -1:
            cost=self.__quantity * FruitInfo.get_fruit_price(self.__fruit_name)
            
            if FruitInfo.get_fruit_price(self.__fruit_name) == max(FruitInfo.get_fruit_price_list()) and self.__quantity>1:
                cost=0.98*cost
            
            elif FruitInfo.get_fruit_price(self.__fruit_name) == min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5:
                cost=0.95*cost
            
            
            if self.__customer.get_cust_type() == "wholesale":
                cost=0.9*cost
            return cost
        
        
        else:
            return -1    
        
    def get_purchase_id(self):
        return self.__purchase_id


    def get_customer(self):
        return self.__customer


    def get_quantity(self):
        return self.__quantity

    

    
class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name = customer_name 
        self.__cust_type = cust_type
        
    def get_cust_type(self):
        return self.__cust_type
    
    def get_customer_name(self):
        return self.__customere_name