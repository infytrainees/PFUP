

#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    x=0
    b=reqd_gems[x] in gems_list
    for x in range (0,len(reqd_gems)):
        needed_gem=reqd_gems[x]
        for a in range (0,len(gems_list)):
            cmp_gem=gems_list[a]
            if (b==True):
                if (gems_list[a]==reqd_gems[x]):
                    crnt_gem_price=price_list[a]
                    req=reqd_quantity[x]
                    bill_amount=bill_amount+price_list[a]*reqd_quantity[x]
                    break
            else:
                bill_amount=-1
                break
    if (bill_amount!=0 and bill_amount>30000):
        dis=(5*bill_amount/100)
        bill_amount=bill_amount-dis
    
    #Write your logic here
    return bill_amount

#List of gems available in the store
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4392, 1342, 8734, 6421]

#List of gems required by the customer
reqd_gems=['Amber', 'Opal', 'Topaz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[2, 1, 3]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
