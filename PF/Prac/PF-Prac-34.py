#PF-Prac-34
def check_well_formatted(input_item,list_label):
    #Start writing your code here
    chk = True
    for item in input_item:
        if type(item) == list:
            chk = check_well_formatted(item, list_label)
        else:
            for i in range (1,len(input_item)):

                if type(input_item[i]) == int:
                    return False
    
    if (input_item[0] in list_label) and len(input_item)>=2 and chk :
        return True
    else:
        return False


input_list1 = [1, [1, 2], '2']
list_label1 = [1, 2]

result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")