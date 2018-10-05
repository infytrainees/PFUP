#DSA-Assgn-2

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

class Service:
    def __init__(self,car_list):
        self.__car_list = car_list 
     
    def get_car_list(self):
        return self.__car_list
    
    def find_cars_by_year(self,year):
        cars_year_wise_list =[]
        for car_object in self.__car_list:
            if car_object.get_year() == year:
                cars_year_wise_list.append(car_object.get_model())
        if len(cars_year_wise_list) == 0:
            return None
        return cars_year_wise_list
         
    
    def add_cars(self,new_car_list):
        
        self.__car_list += new_car_list
        self.__car_list.sort(key=lambda car : car.get_year(), reverse=False)
            
    def remove_cars_from_karnataka(self):
        carlist = self.__car_list
        self.__car_list=[]
        for car in carlist:
            
            if car.get_registration_number()[:2] != 'KA':
                self.__car_list.append(car)
#Implement Service class here

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "KA10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
car_list1=[car1, car2, car3, car4,car5]
ser=Service(car_list)
ser.add_cars(car_list1)
#Create object of Service class, invoke the methods and test your program
