"""
187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.


Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """O(N) / O(N)"""
        m, k, alias = dict(), 0, {"A": 1, "C": 2, "G": 3, "T": 4}
        for i, ch in enumerate(s):
            k = (k % 10 ** 9) * 10 + alias[ch]
            if i >= 9:
                m[k] = m.get(k, 0) + 1
        alias = {v: k for k, v in alias.items()}
        return ["".join(alias[int(ch)] for ch in str(k)) for k, v in m.items() if v > 1]
