"""
1.1 Is Unique: 
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures? 
"""


def solution(string: str) -> bool:
    """
    >>> solution("")
    True
    >>> solution("a")
    True
    >>> solution("abc")
    True
    >>> solution("aabc")
    False
    >>> solution("abbc")
    False
    >>> solution("abcc")
    False
    """
    n = len(string)
    if n == 0:
        return True
        
    checker = set()  # hash table
    for ch in string:
        if ch in checker:
            return False
        checker.add(ch)
        
    return True
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
