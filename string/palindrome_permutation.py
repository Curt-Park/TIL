"""
1.4 Palindrome Permutation: 
Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat". "atco cta". etc.) 
"""


def solution(s: str) -> bool:
    """
    >>> solution("")
    True
    >>> solution("a")
    True
    >>> solution("aA")
    True
    >>> solution("Tact Coa")
    True
    >>> solution("abb")
    True
    >>> solution("abA")
    True
    >>> solution("abc")
    False
    """
    
    checker = {}
    for ch in s:
        if ch == " ":
            continue
            
        ch = ord(ch)
        if ord("A") <= ch <= ord("Z"):
            ch -= ord("A")
        elif ord("a") <= ch <= ord("z"):
            ch -= ord("a")
        
        if not ch in checker:
            checker[ch] = 1
        else:
            checker[ch] += 1
            
    has_odd = False
    for k in checker:
        if checker[k] % 2 == 1:
            if not has_odd:
                has_odd = True
            else:
                return False
            
    return True
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
