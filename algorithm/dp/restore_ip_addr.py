"""
https://leetcode.com/problems/restore-ip-addresses/submissions/

93. Restore IP Addresses
Medium

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """O(1) / O(1)"""
        def seekAllIpAddr(remain = s, ip = "", depth = 0, n = 0):
            if not remain or depth == 5:
                if depth == 4: ans.append(ip[:-1])
                return
            for i in range(min(3, len(remain))):
                n = n * 10 + int(remain[i])
                if n <= 255 and not (n == 0 and i > 0) and not (n < 10 and i > 0):
                    seekAllIpAddr(remain[i+1:], ip + remain[:i+1] + ".", depth + 1)
                else: break
        ans = []; seekAllIpAddr()
        return ans
