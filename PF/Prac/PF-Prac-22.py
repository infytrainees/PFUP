#PF-Tryout
def diagonal_stars(number):
    for x in range (number):
        i=0
        while (i<x):
            i+=1
            print ('.',end='')
        print ('*')
        
   #start writing your code here

number=100    
diagonal_stars(number)