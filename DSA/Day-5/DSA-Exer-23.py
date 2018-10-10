#DSA-Exer-23

def arrange_tickets(tickets_list):
    '''Creating a list with 20 empty spaces'''   
    vacant = [0]*20
    for num in tickets_list:
        '''poping 0 from the list and inserting at the specific index'''
        vacant.pop(int(num[1:])-1)
        vacant.insert(int(num[1:])-1,num)
    '''replacing 0 with V for reference'''
    for x in range (len(vacant)):
        if vacant[x]==0:
            vacant[x]="V"
    """splitting the list into 2 strings with 10 elements each"""
    first_ten = vacant[:10] 
    next_ten  = vacant[10:]
    """removing V from second list"""
    while "V" in next_ten:
        next_ten.remove("V")
    '''popping the 0th index element from second list to the place of every V'''
    for i in range (len(first_ten)):
        if first_ten[i] == "V":
            first_ten.pop(i)
            first_ten.insert(i,next_ten.pop(0))
    return first_ten
    #Remove pass and write your logic here
    pass

tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
