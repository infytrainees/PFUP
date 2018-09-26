#PF-Assgn-50

def sms_encoding(data):
    data=data.split()
    vow,data1=['a','e','i','o','u','A','E','I','O','U'],[]
    count=0
    
    for word in data:
        stt=''
        for chr in word:
            if chr in vow:
                count+=1
            else:
                stt+=chr
        if count == len(word) or len(word)==1:
            data1.append(word)
        else:
            data1.append(stt)
    data1=' '.join(data1)
    return data1

data="I love Python"
print(sms_encoding(data))

