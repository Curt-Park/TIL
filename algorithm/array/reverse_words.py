"""
https://www.interviewcake.com/question/python3/reverse-words?course=fc1&section=array-and-string-manipulation

Your team is scrambling to decipher a recent message, 
worried it's a plot to break into a major European National Cake Vault. 
The message has been mostly deciphered, but all the words are backward! 
Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters 
and reverses the order of the words in place. 

For example:

  message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

When writing your function, assume the message contains only letters and spaces,
and all words are separated by one space.
"""


def reverse_array(arr, i, j):
    """
    >>> arr = list('mutable')
    >>> reverse_array(arr, 0, len(arr) - 1)
    >>> arr
    ['e', 'l', 'b', 'a', 't', 'u', 'm']
    """
    n = j - i + 1

    for k in range(n // 2):
        left, right = i + k, i + n - k - 1
        arr[left], arr[right] = arr[right], arr[left]


def reverse_words(arr):
    """
    >>> arr1 = []
    >>> arr2 = ['a']
    >>> arr3 = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
    >>> reverse_words(arr1)
    >>> reverse_words(arr2)
    >>> reverse_words(arr3)
    >>> ''.join(arr1)
    ''
    >>> ''.join(arr2)
    'a'
    >>> ''.join(arr3)
    'steal pound cake'
    """
    n = len(arr)

    if n <= 1:
        return

    reverse_array(arr, 0, n - 1)

    i = 0
    for j in range(n + 1):
        if j == n or arr[j] == ' ':
            reverse_array(arr, i, j - 1)
            i = j + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

