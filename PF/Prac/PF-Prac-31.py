#PF-Prac-31
def sum_of_elements(num_list,number):
    tmp=[]
    for x in range (0, len(num_list)):
        if num_list[x]==number and x==0:
            tmp.append(num_list[x])
            tmp.append(num_list[x+1])
        
        elif num_list[x]==number and x==len(num_list)-1:
            tmp.append(num_list[x-1])
            tmp.append(num_list[x])
        
        elif num_list[x]==number :
            tmp.append(num_list[x-1])
            tmp.append(num_list[x])
            tmp.append(num_list[x+1])
    
    for i in tmp:
        if i in num_list:
            num_list.remove(i)
    
    if len(num_list) ==0:
        return 0
    return sum(num_list)
      
num_list=[1, 3, 5, 7, 10, 1, 7, 100]
number=7
print(sum_of_elements(num_list, number))