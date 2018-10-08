#DSA-Assgn-15

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Queue
class Job:
    def __init__(self,name,time_needed):
        self.__name = name
        self.__time_needed = time_needed  
        self.__time_elapsed = 0 

    def get_name(self):
        return self.__name


    def get_time_needed(self):
        return self.__time_needed


    def get_time_elapsed(self):
        return self.__time_elapsed


    def __str__(self):
        pass
    def elapsed_time(self,no_of_mins):
        self.__time_elapsed += no_of_mins
        if self.__time_elapsed == self.__time_needed:
            return True
        return False
    
class Employee:
    def __init__(self,name):
        self.__name = name 
        self.__allocated_job = None

    def get_name(self):
        return self.__name


    def get_allocated_job(self):
        return self.__allocated_job


    def set_allocated_job(self, allocated_job):
        self.__allocated_job = allocated_job


    def elapsed_time(self,no_of_mins):
        self.__allocated_job.elapsed_time(no_of_mins)
        pass
   

class Company:
    def __init__(self,emp_list): 
        self.__employees = emp_list
        self.__pending_jobs = None

    def get_employees(self):
        return self.__employees


    def get_pending_jobs(self):
        return self.__pending_jobs

        

    def allocate_new_job(self,job):
        pass 
    def elapsed_time(self,no_of_mins):
        pass    
    

#Implement Job, Employee and Company classes here

#Change the values and test your programH

emp1=Employee("Ken")
emp2=Employee("Henry")
emp3=Employee("Jack")
emp4=Employee("Hen")
emp5=Employee("Jill")
emp_list=[emp1,emp2,emp3,emp4,emp5]
company=Company(emp_list)
job1=Job("job1",50)
job2=Job("job2",45)
job3=Job("job3",35)
job4=Job("job4",400)
job5=Job("job5",30)
job6=Job("job6",30)
job7=Job("job7",50)
job8=Job("job8",25)
company.allocate_new_job(job1)
company.allocate_new_job(job2)
company.allocate_new_job(job3)
company.allocate_new_job(job4)
company.allocate_new_job(job5)
company.allocate_new_job(job6)
company.allocate_new_job(job7)
company.allocate_new_job(job8)
print("Initial allocation:")
for emp in company.get_employees():
    print(emp.get_name(),"is allocated",emp.get_allocated_job().get_name())
print()
print("Pending Jobs:")
company.get_pending_jobs().display()
completed_jobs=company.elapsed_time(30)
'''print("Completed Jobs :")
for job in completed_jobs:
    print(job.name)'''

print("After completion:")
for emp in company.get_employees():
    print(emp.get_name(),"needs", emp.get_allocated_job().get_time_needed()-emp.get_allocated_job().get_time_elapsed(),"more minutes for",emp.get_allocated_job().get_name())
    print()
print("Pending Jobs:")
company.get_pending_jobs().display()
completed_jobs=company.elapsed_time(10)
print("After completion:")
for emp in company.get_employees():
    print(emp.get_name(),"needs", emp.get_allocated_job().get_time_needed()-emp.get_allocated_job().get_time_elapsed(),"more minutes for",emp.get_allocated_job().get_name())
    print()
print("Pending Jobs:")
company.get_pending_jobs().display()