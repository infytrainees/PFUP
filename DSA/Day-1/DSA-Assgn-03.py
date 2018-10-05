#DSA-Assgn-3

def check_double(list1,list2):
    new_list=[]
    for ele in list1:
        if ele*2 in list2:
            new_list.append(ele)    
    return new_list

list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))