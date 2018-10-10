#PF-Prac-29
def exchange_list(number_list):
    mid = len(number_list)//2
    number_list = number_list[:mid-1:-1]+number_list[:mid]   
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))