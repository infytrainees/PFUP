#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    #Write your logic here
    s1=num2+num3
    s2=num1+num3
    s3=num2+num1
    if num1<s1 and num2<s2 and num3<s3:
        return success
    else:
        return failure
    #Use the following messages to return the result wherever necessary
    #Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)
