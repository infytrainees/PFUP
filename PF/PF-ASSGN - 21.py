#PF-Tryout
def generate_next_date(day,month,year):
    #Start writing your code here
    leap=False
    next_day=0
    next_month=month
    next_year=year
    if year%4 ==0 or (year%100==0 and year%400==0):
        leap = True
    else:
        leap = False
    
    if month == 2 and leap == True:
        if day==29:
            next_day=1
            next_month=month+1
        else:
            next_day=day+1
    elif month==2 and leap==False:
        if day==28:
            next_day=1
            next_month=month+1
        else:
            next_day=day+1
    elif  (month ==1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12):
        if day==31:
            next_day=1
            next_month=month+1
            if month==12:
                next_year=year+1
                next_month=1
        else:
            next_day=day+1
    elif (month ==4 or month ==6 or month ==9 or month ==11):
        if day==30:
            next_day=1
            next_month=month+1
        else:
            next_day=day+1
    print ("%d-%d-%d" % (next_day,next_month,next_year))
generate_next_date(23,9,1996)
