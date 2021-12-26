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

def solution(s1: str, s2: str) -> bool:
    """
    >>> solution("pale", "ple")
    True
    >>> solution("pales", "pale")
    True
    >>> solution("pale", "pales")
    True
    >>> solution("pale", "bale")
    True
    >>> solution("pale", "bake")
    False
    >>> solution("pale", "bae")
    False
    >>> solution("", "")
    False
    >>> solution("", "A")
    True
    >>> solution("A", "")
    True
    >>> solution("A", "A")
    False
    >>> solution("teacher", "detacher")
    False
    """
    n1, n2 = len(s1), len(s2)

    if n1 == n2:  # check replace
        cnt_diff = 0
        for i in range(n1):
            if s1[i] != s2[i]:
                cnt_diff += 1

        if cnt_diff == 1:
            return True

    elif n1 + 1 == n2:  # check insert
        ins_pos = 0
        for i in range(n1):
            if s1[i] != s2[i]:
                ins_pos = i
                break
        else:
            return True

        if (s1[:ins_pos] == s2[:ins_pos] and
            s1[ins_pos:] == s2[ins_pos+1:]):
            return True

    elif n1 == n2 + 1:  # check remove
        rem_pos = 0
        for i in range(n2):
            if s1[i] != s2[i]:
                rem_pos = i
                break
        else:
            return True

        if (s2[:rem_pos] == s1[:rem_pos] and
            s2[rem_pos:] == s1[rem_pos+1:]):
            return True

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
