#OOPR-Assgn-11
#Start writing your code here
class Flower:
    
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None 
    
    "Getter Methods are declared below"
    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available

    "Setter Methods are declared below"
    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
        
    "Logical Expressions Starts here"
    
    def validate_flower(self):
        flower_list=['orchid','rose','jasmine']
        if self.__flower_name.lower() in flower_list:
            return True
        else:
            return False
      
    def validate_stock(self,required_quantity):
        
        if self.__stock_available >= required_quantity:
            return True
        else:
            return False
    
    def sell_flower(self,required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available-=required_quantity
            return True
        return False
                    
    def check_level(self):
        "Given Table is Declared here for comparision purposes"
        flower_list=['orchid','rose','jasmine']
        level=[15,25,40]
        if self.validate_flower():
            if self.__stock_available < level[flower_list.index(self.__flower_name.lower())]:
                return True
        return False 