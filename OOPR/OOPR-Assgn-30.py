#OOPR-Assgn-30
#Start writing your code here
class Customer:
    
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def validate_quantity(self):
        if self.__quantity in range (1,6):
            return True
        return False

    def get_customer_name(self):
        return self.__customer_name


    def get_quantity(self):
        return self.__quantity
    
class Pizzaservice:
    counter = 100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id =None
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = None


    def validate_pizza_type(self):
        if self.get_pizza_type().lower() in ["small","medium"]:
            return True
        return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            if self.__pizza_type.lower() == "small":
                if self.__additional_topping:
                    cost = self.__customer.get_quantity()*(150+35)
                else:
                    cost = self.__customer.get_quantity()*(150)
                Pizzaservice.counter+=1
                self.__service_id = "S"+str(Pizzaservice.counter)
            elif self.__pizza_type.lower() == "medium":
                if self.__additional_topping:
                    cost = self.__customer.get_quantity()*(200+50)
                else:
                    cost = self.__customer.get_quantity()*(200)
                Pizzaservice.counter+=1
                self.__service_id = "M"+str(Pizzaservice.counter)
            self.pizza_cost = cost

        else:
            self.pizza_cost = -1
    def get_service_id(self):
        return self.__service_id


    def get_customer(self):
        return self.__customer


    def get_pizza_type(self):
        return self.__pizza_type


    def get_additional_topping(self):
        return self.__additional_topping

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge = 0
        self.__distance_in_kms = distance_in_kms
    
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range (1,11):
            return True
        return False
    
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms <=5:
                    self.__delivery_charge = self.__distance_in_kms * 5
                elif self.__distance_in_kms >5:
                    self.__delivery_charge = ((self.__distance_in_kms-5) * 7)+(25)
                self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1
                 
    def get_delivery_charge(self):
        return self.__delivery_charge


    def get_distance_in_kms(self):
        return self.__distance_in_kms
    
c1=Customer('Asha' , 5)
#Customer(customer_name:Asha , quantity:5),
d1=Doordelivery(c1,"medium",False,11)
a=d1.calculate_pizza_cost()
#distance_in_kms-11,additional_topping-False
