#OOPR-Assgn-32
#Start writing your code here
from abc import abstractmethod,ABCMeta
class Employee(metaclass = ABCMeta):
    def __init__(self,job_band,employee_name,basic_salary,qualification):
        self.__job_band=job_band
        self.__employee_name=employee_name
        self.__basic_salary=basic_salary
        self.__qualification=qualification

    def get_job_band(self):
        return self.__job_band

    def get_employee_name(self):
        return self.__employee_name

    def get_basic_salary(self):
        return self.__basic_salary

    def get_qualification(self):
        return self.__qualification
    @abstractmethod
    def validate_job_band(self):
        pass

    def validate_basic_salary(self):
        if self.__basic_salary>3000:
            return True
        return False

    def validate_qualification(self):
        if self.__qualification in ["Bachelors", "Masters"]:
            return True
        return False

    @abstractmethod
    def calculate_gross_salary(self):
        pass
    
class Graduate(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,cgpa):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa=cgpa
    def get_cgpa(self):
        return self.__cgpa
    def validate_job_band(self):
        if super().get_job_band() in ['A','B','C']:
            return True
        return False
    def calculate_gross_salary(self):
        
        if self.validate_job_band() and self.validate_qualification() and self.validate_basic_salary() :
            gpa = self.__cgpa
            job_band=super().get_job_band()
            if 4<=gpa<=4.25 :
                tpi =1000
            elif 4.26<=gpa<=4.5:
                tpi =1700
            elif 4.51<=gpa<=4.75:
                tpi =3200
            elif 4.76 <=gpa<= 5:
                tpi =5000
            
            if job_band =="A":
                incentive  = 0.04
            elif job_band =="B":
                incentive  = 0.06
            elif job_band =="C":
                incentive  = 0.10
            basic=super().get_basic_salary()
            salary = (basic * incentive)+(basic*0.12)+tpi+basic
            return salary
        return -1

class Lateral(Employee):
    def __init__(self,job_band,employee_name,basic_salary,qualification,skill_set):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set = skill_set
    def get_skill_set(self):
        return self.__skill_set
    def validate_job_band(self):
        if super().get_job_band() in ['D','E','F']:
            return True
        return False
    def calculate_gross_salary(self):
        
        if self.validate_job_band() and self.validate_basic_salary() and self.validate_qualification():
            skill= self.__skill_set
            job_band = super().get_job_band()
            if job_band =="D":
                incentive  = 0.13
            elif job_band =="E":
                incentive  = 0.16
            elif job_band =="F":
                incentive  = 0.20
            if skill == "AGP":
                sme=6500
            elif skill == 'AGPT':
                sme=8200
            elif skill == "AGDEV":
                sme=11500
            else: 
                sme=0
            basic=super().get_basic_salary()
            salary = (basic*1.12) + (basic*incentive) + sme
            return salary
        return -1
