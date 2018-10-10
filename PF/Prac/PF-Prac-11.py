#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    result_list=[0,0]
    for x in sentence:
        if x.islower():
            result_list[1]+=1
        elif x.isupper():
            result_list[0]+=1
    return result_list

sentence="Come Here!!!!!!21qqwwqqSDA"
print(find_upper_and_lower(sentence))
