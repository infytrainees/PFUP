#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    list2.reverse()
    reversed(list2)
    for x in range (0,len(list1)):
        if list1[x] is None:
            list1[x] = ""
        if list2[x] is None:
            list2[x] = ""
        merged_data += list1[x]+list2[x]+" "
    
    resultant_data = merged_data.strip()
    return resultant_data

list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)