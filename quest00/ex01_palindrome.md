Write pseudocode for a function that checks if a string is a palindrome.

    write a function name for the palindrome - isPalindrome
    use string slicing to move through the string
    reverse the string starting at the last index
    comapre the reversed string with the original string
    test the logic with an input


Implement your solution in Python.

def isPalindrome(s):
    return s == s[::-1] 
    
    #this moves through the string from the first index to the last and reverses it
    # the logic then compares the reversed with original string
    # returns True if there is a match and False if there is no match


print (isPalindrome("racecar"))
print (isPalindrome("hello"))
print (isPalindrome("A man a plan a canal Panama"))


Use AI to learn
Now that your function works, use AI to go deeper:

    What's the time complexity?

        s[::-1] creates a full reversed copy of the string
        → O(n) time, O(n) extra space

        Comparing two strings of length n
        → O(n) time (worst case)

        Overall

        Time complexity: O(n)
        Space complexity: O(n) (because of the reversed copy)


    What edge cases might I miss?
    -   Case sensitivity
    -   Spaces and punctuation
    -   Punctuation & symbols
    -   Unicode / accents (depends on expectations)
    -   Empty and single-character strings


    Are there better approaches?"
        Two pointers function 
        -   Less memory
        -   No reversed copy → O(1) extra space


Reflection

    What did you learn from solving it before asking AI?

        I learnt how to reverse a string to form a new string and at the same time, compare it with the original string.

    How is your understanding different now?

        I now understand that, it is not just about reversing and comparing the string, a lot of other things are to be considered
        like the character case of the string (either upper or lower), the punctuation if its a phrase, special characters and numbers.
        Also, the time it takes to execute my code and the memory usage are all critical issues to be considered.

    Could you now write similar functions (e.g., reverse a string) without help?

        Yes, I can now write a function to reverse a string properly without help!