#PF-Assgn-48

def find_correct(word_dict):
    correct=0
    almost=0
    wrong=0
    lst=[]
    for ky, wrd in word_dict.items():
        mis=0
        if ky== wrd :
            correct+=1
        elif len(ky)== len(wrd):
            for i in range (0, len(ky)):
                if ky[i]!=wrd[i]:
                    mis+=1

        if mis>2 or len(ky)!= len(wrd):
            wrong+=1
        elif 0<mis<=2:
            almost+=1
    lst=[correct,almost,wrong]
    return lst
                
word_dict={'POLICY': 'POLICY', 'WIND': 'WIPE', 'WELCOME': 'WELL'}
#word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
