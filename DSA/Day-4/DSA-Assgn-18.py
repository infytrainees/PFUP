#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    text = text.split(" ")
    unknown = []
    for word in text:
        if word not in vocabulary:
            unknown.append(word)
            
    if len(unknown)==0:
        return -1
    return set(unknown)
    #Remove pass and write your logic here
    pass

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)