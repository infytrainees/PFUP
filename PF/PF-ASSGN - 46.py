#PF-Assgn-46
def nearest_palindrome(number):
    number +=1
    num_string = str(number)
    while num_string != num_string[::-1]:
        number +=1
        num_string = str(number)
    return number
         
    #start writitng your code here
number=121
print(nearest_palindrome(number))
