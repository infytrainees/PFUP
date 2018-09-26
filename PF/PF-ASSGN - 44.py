#PF-Assgn-44

def find_duplicates(list_of_numbers):
    lst=[]
    lst1=[]
    for x in list_of_numbers:
        if list_of_numbers.count(x)>1:
            lst.append(x)
        for i in lst:
            if i not in lst1:
                lst1.append(i)
 
    return lst1
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
