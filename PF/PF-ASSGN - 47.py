#PF-Assgn-47
def encrypt_sentence(sentence):
    sen=sentence.split()
    vo=['a','e','i','o','u']
    odds=[]
    for x in range (0,len(sen)):
        if x%2==0: #even words
            sen[x]=sen[x][::-1]
        else:       #odd words
            wrd=sen[x]  #putting word into variable
            b=''        #emptystring to capture vowels
            for chr in wrd: 
                for vow in vo:
                    if chr==vow:
                        b+=vow   #found vowels will be stored in seq order
                        break   #to save time we break when it is found
            for letter in b:            #for combining the vowels and word
                z=wrd.index(letter)     #receives index of first vowel 
                wrd=wrd[0:z]+wrd[z+1:]  #
            sen[x]=(wrd+''.join(b))
    return (' '.join(sen))
    
sentence="WelCome to Mysore and here enjoy the subtle stay"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
