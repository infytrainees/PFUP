#PF-Assgn-37
#Global variables
child_id=(101, 201, 301, 401, 501)
chocolates_received=[10, 5, 3, 2, 4]
def calculate_total_chocolates():
    a=len(chocolates_received)
    tot=0
    for x in range (0,a):
        tot+=chocolates_received[x]
    return tot
    
def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates<1:
        print("Extra chocolates is less than 1")
    elif child_id.count(child_id_rewarded)==0:
        print("Child id is invalid")
    else:
        i=child_id.index(child_id_rewarded)
        chocolates_received[i]= (chocolates_received[i]+extra_chocolates)
        print(chocolates_received)
        #Remove pass and write your logic here
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
        
print(calculate_total_chocolates())

reward_child(301,1)
