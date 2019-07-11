"""
1.6 String Compression: 
Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""

def solution(s: str) -> str:
    """
    >>> solution('aabcccccaaa')
    'a2b1c5a3'
    >>> solution('aaaaa')
    'a5'
    >>> solution('abcdef')
    'abcdef'
    >>> solution('')
    ''
    """
    n = len(s)
    
    if n == 0:
        return s
        
    ret = [s[0]]
    
    cnt = 1
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            ret.append(str(cnt))
            ret.append(s[i])
            cnt = 1
    ret.append(str(cnt))
    
    ret = "".join(ret)
    if n <= len(ret):
        return s
        
    return ret
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
