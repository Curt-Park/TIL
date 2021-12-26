"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. can you do this in place?
"""

from copy import deepcopy
from typing import List


def solution(mat: List[List[int]]) -> List[List[int]]:
    """ space complexity: O(1)
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

    offset = 0
    for i in range(n, 1, -2):  # 6 -> 4 -> 2 or 7 -> 5 -> 3
        for j in range(i - 1):
            tmp_top = mat[offset][offset+j]
            # left to top
            mat[offset][offset+j] = mat[i-1-j+offset][offset]
            # bottom to left
            mat[i-1-j+offset][offset] = mat[i-1+offset][i-1-j+offset]
            # right to bottom
            mat[i-1+offset][i-j-1+offset] = mat[j+offset][i-1+offset]
            # top to right
            mat[j+offset][i-1+offset] = tmp_top

        offset += 1

    return mat


def solution2(mat: List[List[int]]) -> List[List[int]]:
    """ space complexity: O(N^2)
    >>> solution2([[]])
    [[]]
    >>> solution2([[2]])
    [[2]]
    >>> solution2([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]
    >>> solution2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """

    n = len(mat)
    if n <= 1:
        return mat

    tmp_mat = deepcopy(mat)
    for i in range(n):
        for j in range(n):
            mat[j][n-i-1] = tmp_mat[i][j]

    return mat


if __name__ == "__main__":
    import doctest
    doctest.testmod()
