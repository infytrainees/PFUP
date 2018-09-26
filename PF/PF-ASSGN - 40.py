#PF-Assgn-40
def is_palindrome(word):
    word1=''.join(reversed(word))
    if word.casefold()==word1.casefold():
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
