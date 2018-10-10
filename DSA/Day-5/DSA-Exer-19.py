#DSA-Exer-19

def swap(num_list, first_index, second_index):
    tmp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = tmp


def find_next_min(num_list,start_index):
    mini = num_list.index(min(num_list[start_index:]))
    return mini

def selection_sort(num_list):
    for x in range (len(num_list)):
        swap (num_list,x,find_next_min(num_list, x))

#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)