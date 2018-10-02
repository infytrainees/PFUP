#OOPR-Exer-13
#Start writing your code here
from abc import ABCMeta, abstractmethod 
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
        self.__consumer_name=consumer_name
    @abstractmethod
    
	def calculate_monthly_rent(self):
        pass

    def get_consumer_number(self):
        return self.__consumer_number

    def get_consumer_name(self):
        return self.__consumer_name

        
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
    
	def validate_base_pack_name(self):
        listofbasepacks=["Silver", "Gold", "Platinum"]
        if self.__base_pack_name not in listofbasepacks :
            self.__base_pack_name = "Silver"
            print ("Base package name is incorrect, set to Silver")
        return True
    
	def calculate_monthly_rent(self):
        listofbasepacks=["Silver", "Gold", "Platinum"]
        rentlist=[350,440,560]
        if self.__subscription_period in range (1,25):
            print(25)
            if self.validate_base_pack_name():
                rent = rentlist[listofbasepacks.index(self.__base_pack_name)]
                if self.__subscription_period > 12:
                    rent = (rent * (self.__subscription_period-1)) / self.__subscription_period
                return rent
        return -1
        
    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subcription_period
