def isPalindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    #The above line check for spaces, punctuation marks and special characters, remove them and then covert the
    #rest of the characters to lower case
    return s == s[::-1] 
    #this checks the string from the first index to the last and reverses the string when passed to see if it 
    # matches the original string even in reversed order


print (isPalindrome("racecar"))
print (isPalindrome("hello"))
print (isPalindrome("A man a plan a canal Panama"))