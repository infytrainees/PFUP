#PF-Prac-37
def sum_of_list(num_list): 
    #Start writing your code here
    #Do not alter the below line
    if len(num_list)!=0:
        lst = num_list
    else:
        return 0
    
    return lst[0] + sum_of_list(lst[1:])

num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)
