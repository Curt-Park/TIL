"""
https://leetcode.com/problems/find-median-from-data-stream/

295. Find Median from Data Stream
Hard

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream
to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:
If all integer numbers from the stream are between 0 and 100,
how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100,
how would you optimize it?
"""


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 0:
            median = self.nums[n // 2 - 1] + self.nums[n // 2]
            median /= 2
        else:
            median = self.nums[n // 2]
        return float(median)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    assert medianFinder.findMedian() == 1.0
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0
