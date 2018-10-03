#OOPR-Assgn-29
#Start writing your code here
from abc import abstractmethod,ABCMeta
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.bill_amount=None
        self.bill_id=None
    @abstractmethod
    def calculate_bill_amount(self):
        pass

    def get_customer_name(self):
        return self.__customer_name


    

class OccasionalCustomer(Customer):
    __counter=1000
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms=distance_in_kms
        self.bill_id = None
        OccasionalCustomer.__counter+=1
        self.bill_id = "O"+str(OccasionalCustomer.__counter)
        #self.bill_amount = 
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range (1, 6):
            return True
        return False
        

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            if self.__distance_in_kms in range (0,3):
                km_charge = 5
            elif self.__distance_in_kms in range (3,6):
                km_charge = 7.5
            delivery = km_charge * self.__distance_in_kms + 50
            self.bill_amount = delivery
            return self.bill_amount
        self.bill_amount = -1
        return self.bill_amount
    def get_distance_in_kms(self):
        return self.__distance_in_kms

class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin=no_of_tiffin
        self.bill_id = None
        RegularCustomer.__counter +=1
        self.bill_id ="R"+str (RegularCustomer.__counter)
    def validate_no_of_tiffin (self):
        if self.__no_of_tiffin in range (1,8):
            return True
        return False
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = 7 * self.__no_of_tiffin * 50
            return self.bill_amount
        self.bill_amount = -1
        return self.bill_amount



    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
        
