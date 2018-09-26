#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count=0
    num_list1=num_list
    while len(num_list1)!=0:
        for x in num_list1:
            if x+num_list[0]==n and len(num_list)!=1 and x!=num_list[0]:
                count+=1
        del num_list1[0]
    return count
    #Remove pass and write your logic here
num_list=[1,2,4,5,6]
n=10
print(find_pairs_of_numbers(num_list,n))
