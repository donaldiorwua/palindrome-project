# Modify your palindrome function to:

    Ignore spaces and punctuation.
    Be case-insensitive.
    Return the position where the string stops being a palindrome (if not one).

# Modification code    

def isPalindrome(s):
    checked = ''.join(c for c in s if c.isalnum()).lower()

    #The above line check for spaces, punctuation marks and special characters, remove them and then covert the characters to lower case if its in upper case

    length = len(checked)       # gets the length of the cleaned string
    for i in range(length // 2):        #Gets the range of the cleaned stgring and divides it by 2
        if checked[i] != checked[length - 1 - i]:       # Picks each character of the sting and compares them at each index
            return f"Failed at index {i}"       # Returns the index where a mismatch occurs.
    
    return True


print (isPalindrome("racecar"))
print (isPalindrome("hello"))
print (isPalindrome("A man a plan a canal Panama"))



# After your first attempt, ask AI:

#    "I modified my palindrome function to handle more cases.
#   Did I miss anything? Can it be more efficient?"

Issues and improvements:

1. The index returned is from the CLEANED string, not the ORIGINAL string
2. Better to return a tuple than a string message
3. Handle edge cases - empty string or only special characters
4. Return the ORIGINAL index, not the cleaned string index


# Reflect on what AI added that you didn't consider initially.

    The AI pointed out clearly the edge case that was not handled in the code especially an empty string and supplying only special characters which are very crucial as they my make my logic to malfunction. Also, I returned the index of the cleaned string which the AI recommends I return the index of the original string.