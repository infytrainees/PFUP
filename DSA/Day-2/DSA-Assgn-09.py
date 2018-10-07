#DSA-Assgn-9

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import LinkedList

def reverse_linkedlist(reverse_list):
    #write your logic here
    lst=[]
    current  = reverse_list.get_head()
    while current:
        lst.append(current.get_data())
        current = current.get_next()
    lst=lst[::-1]
    link_list = LinkedList()
    for x in lst:
        link_list.add(x)
    reverse_list = link_list
         
    return reverse_list

#Add different values to the linked list and test your program
reverse_list=LinkedList()
reverse_list.add(10)
reverse_list.add(15)
reverse_list.add(14)
reverse_list.add(28)
reverse_list.add(30)
reversed_linkedlist=reverse_linkedlist(reverse_list)
reversed_linkedlist.display()