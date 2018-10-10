#PF-Prac-24
def find_gcd(num1,num2):
    g1,g_fac1 = num1//2,[num1]
    g2,g_fac2 = num2//2,[num2]
    while g1 != 0 :
        if num1%g1 == 0:
            g_fac1.append(g1)
        g1-=1
        
    while g2 != 0:
        if num2%g2 == 0:
            g_fac2.append(g2)
        g2-=1

    for x in g_fac1:
        for y in g_fac2:
            if x == y:
                return x
num1=45
num2=1135
print(find_gcd(num1,num2))