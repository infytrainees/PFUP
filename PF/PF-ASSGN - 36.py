#PF-Assgn-36
def create_largest_number(number_list):
    a=sorted(number_list,reverse=True)
    lar=0
    for x in range (0, len(a)):
        zer=(len(a)-1)*2
        zer=a[0]*(10**zer)
        del a[0]
        lar+=zer
    return lar
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
