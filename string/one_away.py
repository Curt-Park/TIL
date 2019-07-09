"""
1.5 One Away:
There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check ifthey are one edit (or zero edits) away. 

EXAMPLE 
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false 
"""

from collections import defaultdict


def solution(s1: str, s2: str) -> bool:
    """
    >>> solution("pale", "ple")
    True
    >>> solution("pales", "pale")
    True
    >>> solution("pale", "bale")
    True
    >>> solution("pale", "bake")
    False
    >>> solution("pale", "bae")
    False
    """
    n1, n2 = len(s1), len(s2)
    cnt_diff = 0
    
    if n1 == n2:  # check replace
        for i in range(n1):
            if s1[i] != s2[i]:
                cnt_diff += 1
                
    else:  # check insert / remove    
        checker = defaultdict(lambda : 0)
    
        for ch in s1:
            checker[ch] += 1
        
        for ch in s2:
            checker[ch] -= 1
 
        cnt_diff = sum(map(abs, checker.values()))

    if cnt_diff > 1:
        return False
           
    return True
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
