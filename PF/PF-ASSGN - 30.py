#PF-Assgn-30

def encode(message):
    a=len(message)
    count=0
    strng=''
    for x in range (0, a-1):
        if message [x]==message[x+1]:
            count+=1
            if x==(a-2) :
                strng=strng+str(count+1)+message[x]
                count=0
        else:
            strng=strng+str(count+1)+message[x]
            count=0
    
    if a>1 and message [a-1]!= message [a-2]:
        strng = strng + '1' + message[-1]
    elif a==1:
            strng = '1'+message
    return strng   
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("AASSDDD")
print(encoded_message)
