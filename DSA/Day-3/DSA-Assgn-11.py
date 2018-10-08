#DSA-Assgn-11

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Queue

def merge_queue(queue1,queue2):
    #write your logic here
    if queue1.get_max_size() > queue2.get_max_size():
        big = queue1
        small = queue2
    else:
        big = queue2
        small = queue1
        
        
    merged_queue = Queue(queue1.get_max_size()+queue2.get_max_size())
    count = 1
    
    for y in range (small.get_max_size()*2):
        if count%2 ==0:
            merged_queue.enqueue(queue2.dequeue())
        else:
            merged_queue.enqueue(queue1.dequeue())
        count +=1
    for x in range (big.get_max_size()-small.get_max_size()):
        merged_queue.enqueue(big.dequeue())
    
    return merged_queue

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()