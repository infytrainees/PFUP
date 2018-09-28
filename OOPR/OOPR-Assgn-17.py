#OOPR-Assgn-17
#Start writing your code here
class Freight:
    counter=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_charge=None
        self.__freight_id=None
        
    def validate_weight(self):
        if self.__weight%5==0:
            return True
        else:
            return False
        
    def validate_distance(self):
        if 500 <= self.__distance <=5000:
            return True
        else:
            return False
    
    def forward_cargo(self):
        #"Condition Starts and continues in multiple Lines
        if self.__recipient_customer.validate_customer_id() and \
        self.__from_customer.validate_customer_id() and \
        self.validate_distance()\
        and self.validate_weight():
            #Condition Ends here
        
        
            Freight.counter+=2
            self.__freight_id=Freight.counter
            self.__freight_charge = (150*self.__weight)+(60*self.__distance)
        else:
            self.__freight_charge = 0
        
   
    def get_recipient_customer(self):
        return self.__recipient_customer
    def get_from_customer(self):
        return self.__from_customer
    def get_weight(self):
        return self.__weight
    def get_distance(self):
        return self.__distance
    def get_freight_charge(self):
        return self.__freight_charge
    def get_freight_id(self):
        return self.__freight_id
        




class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address

    def validate_customer_id(self):
        
        if(200000>self.__customer_id>=100000):
            return True
        else:
            return False

    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_address(self):
        return self.__address