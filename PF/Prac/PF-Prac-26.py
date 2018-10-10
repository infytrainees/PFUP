#PF-Prac-26
def check_occurence(string):
    string = string.lower()
    if (string.count("jet") == string.count("mat")):
        return True
    return False
    #start writing your code here
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))