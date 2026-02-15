def isPalindrome(s):
    return s == s[::-1] 
    
    #this checks the string from the first index to the last and reverses the string when passed to see if it 
    # matches the original string even in reversed order


print (isPalindrome("racecar"))
print (isPalindrome("hello"))
print (isPalindrome("A man a plan a canal Panama"))


Reflection
I learnt how to reverse a string to form a new string and at the same time, compare it with the original string.

I now understand that, it is not just about reversing and comparing the string, a lot of other things are to be considered
like the letter case of the string (either upper or lower), the punctuation if its a phrase, special characters and numbers.

Yes, I can now write a function to reverse a string properly now!