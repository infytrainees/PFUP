#DSA-Assgn-7

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import LinkedList

def remove_duplicates(duplicate_list):
    #write your logic here
    current = duplicate_list.get_head()
    nxt = current.get_next()
    while nxt :
        if current.get_data() == nxt.get_data():
            delete = current
            duplicate_list.delete(delete.get_data())
            current = nxt
            nxt = nxt.get_next()
        else:
            current = nxt
            nxt = nxt.get_next()       
    return duplicate_list

#Add different values to the linked list and test your program
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

remove_duplicates(duplicate_list)