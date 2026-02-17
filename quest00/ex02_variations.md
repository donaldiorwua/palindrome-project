Modify your palindrome function to:

    Ignore spaces and punctuation.
    Be case-insensitive.
    Return the position where the string stops being a palindrome (if not one).

def isPalindrome(s):
    checked = ''.join(c for c in s if c.isalnum()).lower()

    #The above line check for spaces, punctuation marks and special characters, remove them and then covert the characters to lower case if its in upper case

    return checked == s[::-1] 

    #this checks the string from the first index to the last and reverses the string when passed to see if it matches the original string even in reversed order and returns the reversed string as a new string


print (isPalindrome("racecar"))
print (isPalindrome("hello"))
print (isPalindrome("A man a plan a canal Panama"))