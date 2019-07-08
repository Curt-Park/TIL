"""
1.2 Check Permutation: 
Given two strings, write a method to decide 
if one is a permutation of the other. 
"""


def solution(str1: str, str2: str) -> bool:
    """
    >>> solution("", "")
    True
    >>> solution("a", "a")
    True
    >>> solution("abcdef", "abcdfe")
    True
    >>> solution("abcdef", "abcde")
    False
    >>> solution("", "abc")
    False
    >>> solution("abc", "")
    False
    """
    return len(set(str1)) == len(set(str2))
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
