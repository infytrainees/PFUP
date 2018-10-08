#DSA-Assgn-13

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Stack

def change_smallest_value(number_stack):
    #write your logic here
    
    tmp =[]
    while not (number_stack.is_empty()):
        pop = number_stack.pop()
        tmp.append(pop)
    mini = min(tmp)
    count = tmp.count(mini)
    
    for i in range (count):
        tmp.remove(mini)
        number_stack.push(mini)
    
    
    for x in tmp[::-1]:
        number_stack.push(x)
    return number_stack
        
        
        
        
        
number_stack=Stack(8)

number_stack.push(4)
number_stack.push(7)
number_stack.push(3)
number_stack.push(3)
number_stack.push(90)
# number_stack.push(4)
# number_stack.push(14)
# number_stack.push(7)

print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()