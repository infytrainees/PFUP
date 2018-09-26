#PF-Assgn-33

def find_common_characters(msg1,msg2):
    msg1=msg1.replace(" ","")
    msg2=msg2.replace(" ","")
    strng=''
    ans=''
    for x in range (0, len(msg1)):
        for y in range (0, len(msg2)):
            if msg1[x]==msg2[y]:
                strng=strng+msg1[x]
    
    for x in range (0, len(strng)):
        if strng[x-1]!=strng[x]:
            ans=ans+strng[x]
    ans=''.join(sorted(set(ans), key=ans.index))
    if len(strng)==0:
        ans=-1
    elif len(strng)==1:
        ans= strng      
    return ans
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="Smoto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
