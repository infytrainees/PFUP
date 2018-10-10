#DSA-Prac-10
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
            
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
            
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    
    def get_max_size(self):
        return self.__max_size
    
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg    

class LunchBox:
    def __init__(self,color,manufacturer):
        self.__color = color 
        self.__manufacturer = manufacturer 
    def get_color(self):
        return self.__color
    def get_manufacturer(self):
        return self.__manufacturer
    def __str__(self):
        print (self__color+"  "+self.__manufacturer)


class Container:
    def __init__(self,box_stack):
        self.__box_stack = box_stack 
    def get_box_stack(self):
        return self.__box_stack 
    def identify_count(self,color):
        
        pass
#start writing your code here
