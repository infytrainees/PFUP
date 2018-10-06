#DSA-Assgn-5
'''imported DatStructures Module from a source folder names "res"'''
from res.DataStructures import LinkedList
def create_new_sentence(word_list):
    new_sentence=""
    tmp = ''
    current = word_list.get_head()
    while (current):
        tmp = current.get_data()
        if tmp == "*" or tmp == "/":
            new_sentence +=" "
        elif new_sentence[-2:] == "  ":
            new_sentence += tmp.upper()
        else:
            new_sentence += tmp
        current = current.get_next()

    new_sentence = new_sentence.replace('  ', ' ') 
    return new_sentence

word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result=create_new_sentence(word_list)
print(result)