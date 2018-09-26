#PF-Assgn-31
def check_palindrome(word):
    reve=''
    for x in range (1,len(word)+1):
        reve=reve+word[-x]
    return (reve==word)
    #Remove pass and write your logic here

status=check_palindrome("MADAM")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
