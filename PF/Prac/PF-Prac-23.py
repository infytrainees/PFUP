#PF-Prac-23
def divisible_by_sum(number):
    if number % 9 == 0:
        sum_of_dig = 9
    else:
        sum_of_dig = number % 9
    
    if number % sum_of_dig ==0:
        return True
    return False

    
number=42
print(divisible_by_sum(number))