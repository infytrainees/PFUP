#OOPR-Assgn-18
#Start writing your code here
class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None
    
    def get_customer_name(self):
        return self.__customer_name 
    
    def get_payment_status(self):
        return self.__payment_status

    def pays_bill(self,bill):
        self.__payment_status="Paid"
    
class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id = None
        self.__bill_amount= None
    
    def get_bill_id(self):
        return self.__bill_id
    
    def get_bill_amount(self):
        return self.__bill_amount
    
    def generate_bill_amount (self,item_quantity,items):
        Bill.counter+=1
        
        self.__bill_amount=0
        self.__bill_id='B'+str(Bill.counter)  #Billid as per logic #B1001,B1002....
        
        tmp_dict=item_quantity  # temporary dict to change case of the items
        #item_quantity={}
        a={}
        
        for item in tmp_dict:
            a[item.lower()]=tmp_dict[item]     #creatina dictionary with lower keys
        
        for prod,quan in a.items():
            for item in items:
                if item.get_item_id().lower()==prod:
                    self.__bill_amount+=quan*item.get_price_per_quantity()
                    break
class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity
        
    def get_item_id(self):
        return self.__item_id
    
    def get_description(self):
        return self.__description
    
    def get_price_per_quantity(self):
        return self.__price_per_quantity
    
t1=Item('Ip789',"cofee",25)
t3=Item('Ip777',"cee",245)
dic={'ir658':4, 'IR987':3, 'IR123':2, 'Ir346':2}

i1=Item('IR987' , 'Sunfeast Marie', 100)
i2=Item('ir658' , 'Kellogs Oats',120)
i3=Item('Ir346' , 'Maggie Noodles',130)
i4=Item('iR234' , 'Kissan Jam',140)
i5=Item('IR123' , 'Nescafe',150)
i6=Item('IR111' , 'Milk',160)

i=[i1,i2,i3,i4,i5,i6]

b1=Bill()
b1.generate_bill_amount(dic, i)