"""
https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/
"""

from collections import deque


class Solution:
    def __init__(self):
        self.buf = deque()

    def read(self, buf, n):
        """ O(N), O(N)
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        cnt, n_read = 0, 4
        tmp = [" "] * 4
        while n > len(self.buf) and n_read == 4:
            n_read = read4(tmp)
            self.buf.extend(tmp[:n_read])
        while self.buf and n > 0:
            buf[cnt] = self.buf.popleft()
            cnt += 1
            n -= 1
        return cnt
