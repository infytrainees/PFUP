#PF-Tryout
def find_five_digit():
    for x in range (2,10): 
        n3 = x
        n2 = x+2
        n4 = x-2
        n1 = (x+2)+2
        n5 = (x-2)+2
        
        if n1+n2+n3+n4+n5==19 and n1==n3+n4+n5:
            number = ''
            for num in [n1,n2,n3,n4,n5]:
                number+=str(num)
            print (int(number))
            break
find_five_digit()