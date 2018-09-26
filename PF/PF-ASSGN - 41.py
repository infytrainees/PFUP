#PF-Assgn-41
def find_ten_substring(num_str):
    num_str=list(map(int,num_str))
    lst,a,=[],len(num_str)
    for x in range (0,a):
        st='' #To put some empty strings 
        z=[] #Temporary list to check sum
        for y in range (x,a):
            st+=str(num_str[y])
            z.append(num_str[y])
            if sum(z)==10:
                lst.append(st)
    return lst
    
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
