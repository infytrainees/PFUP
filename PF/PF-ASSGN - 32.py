#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    b=patient_medical_speciality_list
    b_len=len(b)
    p_count, o_count, e_count = 0,0,0   
    for x in range (1,b_len,2):
        if b[x]=='P':
            p_count+=1
        elif b[x]=='O':
            o_count+=1
        elif b[x]=='E':
            e_count+=1
    if (p_count > e_count) and (p_count > o_count):
        speciality=medical_speciality['P']
    elif (e_count > p_count) and (e_count > o_count):
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
