"""
https://www.interviewcake.com/question/python3/reverse-string-in-place?course=fc1&section=array-and-string-manipulation

Why a list of characters instead of a string?
The goal of this question is to practice manipulating strings in place. 
Since we're modifying the input, we need a mutable.
"""


def reverse_array(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
        
    for i in range(n // 2):
        left, right = i, n - i - 1
        arr[left], arr[right] = arr[right], arr[left]
        
    return arr
    
    
assert [] == reverse_array([])
assert ['a'] == reverse_array(list('a'))
assert ['e', 'l', 'b', 'a', 't', 'u', 'm'] == reverse_array(list('mutable'))
