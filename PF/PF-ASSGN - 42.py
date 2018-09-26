#PF-Assgn-42
def find_factors(num):
    
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    prime=0
    for x in list_of_factors:
        if is_prime(x,x//2):
            prime=x
    return prime

def find_f(num):
    return find_largest_prime_factor(find_factors(num))

def find_g(num):
    s=0
    for x in range (num,num+9):
        s+=find_f(x) 
    return s

print(find_g(10))
