#PF-Prac-15
def check_22(num_list):
    for x in range (1,len(num_list)):
        if num_list[x-1] == 2 and num_list[x] ==2:
            return True
    return False
    #start writing your code here
        
print(check_22([3,2,5,1,2,1,2,52]))