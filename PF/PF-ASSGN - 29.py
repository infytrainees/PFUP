#PF-Assgn-29
def calculate(distance,no_of_passengers):
    amount_received=80*no_of_passengers
    actual_price=(distance/10)*70
    if actual_price<amount_received:
        return (amount_received-actual_price)
    else:
        return(-1)
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
