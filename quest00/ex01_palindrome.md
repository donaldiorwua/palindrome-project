## Write pseudocode for a function that checks if a string is a palindrome.
   Start
    - write a function name for the palindrome - isPalindrome
    - clean up the string by checking for spaces, punctuations, alphnumeric characters  
      and covert all character case to lower case.
    - use string slicing to move through the string, reverse the string starting at the   
      last index
    - comapre the reversed string with the original string to check if they match
    - Test the function with inputs
  End 


## Implement your solution in Python.

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



## Use AI to learn

Now that your function works, use AI to go deeper:

#    What's the time complexity?

#       Time complexity

            Let n = length of the input string

            Breakdown

            isalnum() + join → O(n)
            .lower() → O(n)
            [::-1] (string reverse) → O(n)
            Comparison → O(n)

            ✅ Total time complexity

            O(n)

        This is optimal — you cannot do better than linear time for palindrome checking.

#       Space (memory) complexity

            You create:

            A new cleaned string (checked)
            A reversed copy (checked[::-1])
            ❗ Space complexity
            O(n) extra space

            This matters for very long strings.

#   What edge cases might I miss?

    -   Only non-alphanumeric characters (symbols) example (!!!)
    -   Very large input (millions of chars)
    -   Unicode / accents (depends on expectations)
    -   Empty and single-character strings


#    Are there better approaches?"

#        Two pointers function 
        -   Less memory
        -   No reversed copy → O(1) extra space

#       Regex-based approach (clean but slower)
        - Very readable
        - Regex adds overhead
        - Still O(n), but slower in practice


# Reflection

#    What did you learn from solving it before asking AI?

        I learnt how to reverse a string to form a new string and at the same time, compare it with the original string. I learnt how to clean a string input i.e the character case of the string ( upper to lower), the punctuation if its a phrase, special characters and numbers.

#    How is your understanding different now?

        I now understand that, it is not just about reversing and comparing the string, a lot of other things are to be considered. Like the worst input to expect example, an empty input, only special character input, unicode/accents.        
        Also, the time it takes to execute my code and the memory usage are all critical issues to be considered.

#    Could you now write similar functions (e.g., reverse a string) without help?

        Yes, I can now write a function to reverse a string properly without help!