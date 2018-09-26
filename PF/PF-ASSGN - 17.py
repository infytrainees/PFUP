#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    if job_level==3:
        new_salary=current_salary+(15*current_salary/100)
    elif job_level==4:
        new_salary=current_salary+(7*current_salary/100)
    elif job_level==5:
        new_salary=current_salary+(5*current_salary/100)
    else:
        new_salary=current_salary+(0*current_salary/100)
    new_salary=int(new_salary)      #converting into integer
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(12500,4)
print(new_salary)
