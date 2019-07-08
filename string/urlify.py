"""
1.3 URLify: 
Write a method to replace all spaces in a string with '%20: You may assume that the string 
has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.) 

EXAMPLE 
Input: "Mr John Smith", 13 
Output: "Mr%20John%20Smith" 
"""

from typing import List

def solution(s: List[str], n: int) -> str:
    """
    >>> solution(list(""), 0)
    ''
    >>> solution(list("Mr John Smith    "), 13)
    'Mr%20John%20Smith'
    >>> solution(list(" Mr John Smith      "), 14)
    '%20Mr%20John%20Smith'
    >>> solution(list("Mr John Smith       "), 14)
    'Mr%20John%20Smith%20'
    >>> solution(list("Mr John  Smith      "), 14)
    'Mr%20John%20%20Smith'
    """
    
    cnt = 0
    for i in range(n):
        if s[i] == " ":
            cnt += 1
    
    for i in reversed(range(n)):
        if s[i] == " ":
            end = i + cnt * 2
            s[end-2:end+1] = list("%20")
            cnt -= 1
        else:
            s[i + cnt * 2] = s[i]   
    
    return "".join(s)
          
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
