#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21,1,1,1,1,2,5,12,25,25,22,12,23)

def find_more_than_average():
    a=len(list_of_marks)
    tot=0
    students=0
    for x in range (0,a):
        tot+=list_of_marks[x]
    avg=tot/a
    for y in range (0,a):
        if list_of_marks[y]>avg:
            students+=1
    return (students*100/a)
    #Remove pass and write your logic here

def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here

def generate_frequency():
    freq=[]
    std=sorted(list_of_marks)
    for x in range (0,26):
        freq.append(std.count(x))
    return freq
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
