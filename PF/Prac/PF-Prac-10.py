#PF-Prac-10
def string_both_ends(input_string):
    #start writing your code here
    if len(input_string)<2:
        return -1
    else:
        return input_string[:2]+input_string[-2:]

input_string="w3w"
print(string_both_ends(input_string))