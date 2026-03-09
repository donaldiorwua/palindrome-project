
def isPalindrome(s):
# this defines the function name
    checked = ''.join(c for c in s if c.isalnum()).lower()

# This line check and joins the characters of the passed string if they are alpha-numeric characters and convert their case into lower case if in upper case
    
    return checked == checked[::-1] 
    
# this moves through the string from the first index to the last and reverses it
# the logic then compares the reversed with original string
# returns True if there is a match and False if there is no match


print (isPalindrome("racecar"))
print (isPalindrome("hello"))
print (isPalindrome("A man a plan a canal Panama"))
