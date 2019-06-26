"""
https://www.interviewcake.com/question/python3/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation

In order to win the prize for most cookies sold, 
my friend Alice and I are going to merge our Girl Scout Cookies orders 
and enter as one unit.
Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. 
Write a function to merge our lists of orders into one sorted list.

For example:

  my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
"""


def merge_lists(list1, list2):
    """
    >>> list1 = [3, 4, 6, 10, 11, 15]
    >>> list2 = [1, 5, 8, 12, 14, 19]
    >>> merge_lists(list1, list2)
    [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    
    >>> list1 = []
    >>> list2 = [1, 5, 8, 12, 14, 19]
    >>> merge_lists(list1, list2)
    [1, 5, 8, 12, 14, 19]
    
    >>> list1 = [3, 4, 6, 10, 11, 15]
    >>> list2 = []
    >>> merge_lists(list1, list2)
    [3, 4, 6, 10, 11, 15]
    
    >>> list1 = []
    >>> list2 = []
    >>> merge_lists(list1, list2)
    []
    
    >>> list1 = [3, 4, 6]
    >>> list2 = [3, 4, 6]
    >>> merge_lists(list1, list2)
    [3, 3, 4, 4, 6, 6]
    """
    i, j, n1, n2 = 0, 0, len(list1), len(list2)
    ret = []
    while i < n1 or j < n2:
        while i < n1 and (j == n2 or list1[i] <= list2[j]):
            ret.append(list1[i])
            i += 1
        while j < n2 and (i == n1 or list2[j] <= list1[i]):
            ret.append(list2[j])
            j += 1
            
    return ret
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
