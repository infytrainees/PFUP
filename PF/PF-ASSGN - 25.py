#PF-Tryout

#debug the below code
counter1=0
counter2=5
while(counter2 >0):
    star="*****"
    while(counter2>counter1):
        star=star[counter1:counter2]
        counter2-=1
        print(star)
    counter1=1
