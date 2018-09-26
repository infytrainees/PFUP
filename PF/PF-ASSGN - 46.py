#PF-Assgn-46
def palindrome(number):
    temp=0
    a=number
    while(number!=0):
        remainder=number%10
        number=number//10
        temp=temp*10+remainder
    if(a==temp):
        return True
    else:    
        return False

def nearest_palindrome(number):
    tmp=number
    while not(palindrome(tmp)):
        tmp+=1
    
    if number == 0:
        return 1
    elif tmp==number:
        return nearest_palindrome(tmp+1)
    else:    
        return tmp
    #start writitng your code here

number=0
print(nearest_palindrome(number))
