#DSA-Exer-22

def order_heights(student_list,height_list):
    for y in range (2):
        for x in range (len(student_list)-1):
            if height_list[x] > height_list[x+1]:
                height_list[x],height_list[x+1] = height_list[x+1], height_list[x]
                student_list[x],student_list[x+1] = student_list[x+1],student_list[x]

    return[student_list,height_list]

#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])