#PF-Assgn-43
def find_factors(num):
    
    factors = []
    for i in range(1,(num+1)):
        if(num%i==0):
            factors.append(i)
    return len(factors)

def find_smallest_number(num):
    ok=True
    n=1
    while ok:
        if num==find_factors(n):
            ok=False
        else:
            n+=1
    return n
    #start writing your code here

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)

#find_factors(120)
