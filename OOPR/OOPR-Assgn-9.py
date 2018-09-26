#OOPR-Assgn-9
#Start writing your code here
class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = [1001,1002]
        self.__fees = [25575,15500]
    def validate_marks(self):
        if self.__marks in range (0,101):
            return True
        else:
            return False
    
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
        
    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.__marks>=65:
            return True
        else:
            return False
    
    def set_student_id(self,student_id):
        self.__student_id=student_id
        
    def set_marks(self,marks):
        self.__marks=marks
    
    def set_age(self,age):
        self.__age=age
    
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_fees(self):
        return self.__fees
    def get_course_id(self):
        return self.__course_id
    
    
    def choose_course(self,course_id):
        if self.check_qualification() and (course_id in self.__course_id):
            
            if self.__marks>85 :
                self.__fees=0.75*self.__fees[self.__course_id.index(course_id)]
            else:
                self.__fees=self.__fees[self.__course_id.index(course_id)]
            self.__course_id=course_id
            
            return True
        else:
            self.__course_id=None
            self.__fees=None
            return False