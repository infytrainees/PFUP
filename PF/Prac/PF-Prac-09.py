#PF-Prac-9
def generate_dict(number):
    new_dict={}
    for i in range (1, number+1):
        new_dict[i]=i**2
    return new_dict

number=20
print(generate_dict(number))