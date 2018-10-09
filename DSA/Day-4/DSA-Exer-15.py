#DSA-Exer-15

def pattern_search(text, pattern):
    #Remove pass and write your logic here
    text = text.split(pattern)
    return (len(text)-1)

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)