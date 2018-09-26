#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    x=0
    while (len(list_of_leap_years)<15):
        if (given_year%4==0) and (given_year%100!=0 or given_year%400==0):
            list_of_leap_years.insert(x,given_year)
            x+=1
            given_year+=4
        else:
            given_year+=1
    return list_of_leap_years

list_of_leap_years=find_leap_years(2001)
print(list_of_leap_years)
