#DSA-Exer-9

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

class People:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender

    def get_name(self):
        return self.__name


    def get_age(self):
        return self.__age


    def get_gender(self):
        return self.__gender


    def __str__(self):
        return(self.__name+" "+str(self.__age)+" "+self.__gender)

    @staticmethod
    def check_gender(people_queue,gender):
        gender_queue = Queue(people_queue.get_max_size())
        while not(people_queue.is_empty()):
            person = people_queue.dequeue()
            if person.get_gender() == gender:
                gender_queue.enqueue(person)
        return gender_queue
            
    # Write the remaining methods of People class here

people1=People("Jack",25,"Male")
people2=People("Tom",30,"Male")
people3=People("Asha",27,"Female")
people4=People("Henry",27,"Male")
people5=People("Tina",27,"Female")

people_queue=Queue(5)
people_queue.enqueue(people1)
people_queue.enqueue(people2)
people_queue.enqueue(people3)
people_queue.enqueue(people4)
people_queue.enqueue(people5)

result_queue=People.check_gender(people_queue, "Male")
result_queue.display()