#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    if(account_number>=1000 and account_number<=1999 and account_balance>=100000):
        if(salary>25000 and loan_type=="Car"):
            eligible_loan_amount=500000
            bank_emi_expected=36
            if(eligible_loan_amount>=loan_amount_expected and bank_emi_expected>=customer_emi_expected):
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            else:
                print("The customer is not eligible for the loan")
                
            
        elif(salary>50000 and loan_type=="House"):
            eligible_loan_amount=6000000
            bank_emi_expected=60
            if(eligible_loan_amount>=loan_amount_expected and bank_emi_expected>=customer_emi_expected):
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            
            else:
                print("The customer is not eligible for the loan")
                
        elif(salary>75000 and loan_type=="Business"):
            eligible_loan_amount=7500000
            bank_emi_expected=84
            if(eligible_loan_amount>=loan_amount_expected and bank_emi_expected>=customer_emi_expected):
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.", eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:",customer_emi_expected)
            
            else:
                print("The customer is not eligible for the loan")
                
        else:
            print("Invalid loan type or salary")

    elif(account_number<1000 or account_number>1999):
        print("Invalid account number")
        
    elif(account_balance<100000):
        print("Insufficient account balance")
        
    else:
        print("The customer is not eligible for the loan")
   
calculate_loan(1005,25000,255000,"Car",300000,30)
#account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected

