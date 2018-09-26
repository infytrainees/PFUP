#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if 0 < distance_in_kms < 3:
        delivery = 0
    elif 0 < distance_in_kms < 6:
        delivery = (distance_in_kms-3)*3
    elif distance_in_kms >=6  :
        delivery = (distance_in_kms-6)*6+(9)
    else:
        delivery = -1
        
    if food_type == 'N':
        cost = quantity_ordered*150
    elif food_type == 'V':
        cost = quantity_ordered*120
    else:
        cost = -1
    
    if (delivery != -1) and (cost != -1) and quantity_ordered > 0:
        bill_amount = cost+delivery
    else:
        bill_amount = -1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,-10)
print(bill_amount)
