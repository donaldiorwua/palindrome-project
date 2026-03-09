def isPalindrome(s):
    checked = ''.join(c for c in s if c.isalnum()).lower()

    #The above line check for spaces, punctuation marks and special characters, remove them and then covert the characters to lower case if its in upper case

    length = len(checked)       # gets the length of the cleaned string
    for i in range(length // 2):        #Gets the range of the cleaned stgring and divides it by 2
        if checked[i] != checked[length - 1 - i]:       # Picks each character of the sting and compares them at each index
            return f"Failed at index {i}"       # Returns the index where a mismatch occurs.
    
    return True


print (isPalindrome("racecar"))
print (isPalindrome("nurse run"))
print (isPalindrome("A man a plan a canal Panama"))
