#DSA-Exer-18

def find_next_min(num_list,start_index):
    mini = num_list.index(min(num_list[start_index:]))
    return mini

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=1
print("Index of the next minimum element is", find_next_min(num_list,start_index))