"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees. can you do this in place? 
"""

from typing import List


def solution(mat: List[List[int]]) -> List[List[int]]:
    """
    >>> solution([[]])
    [[]]
    >>> solution([[2]])
    [[2]]
    >>> solution([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]
    >>> solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    
    n = len(mat)
    if n <= 1:
        return mat
        
    tmp_mat = mat.copy()
    for i in range(n):
        for j in range(n):
            mat[j][n-i-1] = tmp_mat[i][j]
        
    return mat

"""  
00 01 02.  20 10 00
10 11 12.  21 11 01
20 21 22.  22 12 02

00 01. 10 00
10 11. 11 01
"""

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
