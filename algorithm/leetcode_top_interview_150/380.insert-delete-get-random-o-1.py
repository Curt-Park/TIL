#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from random import choice

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        last = self.l[-1]
        idx = self.d[val]
        self.l[-1], self.l[idx] = self.l[idx], self.l[-1]
        self.d[last] = idx
        self.l.pop()
        self.d.pop(val)
        return True
        

    def getRandom(self) -> int:
        return choice(self.l) 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

