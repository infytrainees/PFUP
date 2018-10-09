#DSA-Assgn-16

from res.DataStructures import Stack,Queue

def separate_boxes(box_stack):
    que = Queue(box_stack.get_max_size())
    lst = []
    while not (box_stack.is_empty()):
        poped = box_stack.pop()
        if poped in ["Red","Blue","Green"]:
            lst.append(poped)
        else:
            que.enqueue(poped)
    while len(lst)!=0:
        box_stack.push(lst.pop())
    return que
            
    #Remove pass and write your logic here
    pass

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()