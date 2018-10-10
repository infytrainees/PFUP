#DSA-Exer-21

def merge_sort(num_list):
    high = len(num_list)-1
    low = 0
    if high == low:
        return num_list
    else:
        mid = len(num_list) //2
        sorted_list = merge (merge_sort(num_list[:mid]),merge_sort(num_list[mid:]))
    return sorted_list
    # Remove pass and write the logic here to return the sorted list
    pass

def merge(left_list,right_list):
    i,j = 0,0
    sorted_list = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append (right_list[j])
            j+=1
    for i in left_list:
        if i not in sorted_list:
            sorted_list.append (i)
    for j in right_list:
        if j not in sorted_list :
            sorted_list.append (j)
    return sorted_list
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    pass

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
