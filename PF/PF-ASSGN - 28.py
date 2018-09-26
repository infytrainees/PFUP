#PF-Assgn-28
from _overlapped import NULL

def sum_of_digits(n):
    rem=0
    ans=0
    while n!=0:
        rem=n%10
        n//=10
        ans=rem+ans
    return ans
def find_max(num1, num2):
    max_num=-1
    n=num1
    lst=[]
    if num1<num2:
        for x in range (num1, num2+1):
            if (sum_of_digits(n)%3==0) and (10<=n<100) and n%5==0:
                lst.append(n)
                n+=1
            else:
                n+=1
        if len(lst)!=0:
            max_num=max(lst)
        else:
            max_num=-1
    else:
        max_num=-1
    # Write your logic here
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,30)
print(max_num)
