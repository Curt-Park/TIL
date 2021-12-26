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

1 2 3 4 5
3 2 1 4 5
5 4 3 2 1
1 2 3 5 4
1 2 3 2 1
5 1 4 2 3
1 5 2 4 3
1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1

min max
1,2
2,3 1
3,4 2,1
3,4,5 2,1

3
2,3
3 2
3 2,1
3,4 2,1
3,4,5 2,1

5
4,5
5 4
5 4,3
5 4,3,2
4,5 3,2
3,4,5 2,1

1,2
2,3 1
3,5 2,1
3,5,4 2,1

1,2
2,3 1
2,3 2,1
2,3 2,1,1

5
1,5
5 1
4,5 1
4,5 2,1
3,4,5 2,1

1
1,5
1,5,2
2,5 1
2,5,4 1
4,5 2,1
4,5 3,2,1

1
2 1
2,3 1
3,4 2,1
4,5 3,2,1
...

9
8,9
9 8
9 8,7
9 8,7,6
8,9 7,6
7,8,9 6,5
...

4
4,5
5 4
5 4,1
5,9 4,1
5,9 4,1,3
4,5,9 3,1,2
5,9,7 4,3,1,2
5,9,6,7 4,3,1,2
5,9,6,7,8 4,3,1,2

"""


import heapq


class MedianFinder2:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


class MedianFinder1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap, self.max_heap = [], []

    def addNum(self, num: int) -> None:
        """O(logN)"""
        if not self.max_heap or -self.max_heap[0] <= num:
            heapq.heappush(self.min_heap, num)
        elif num <= self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        elif num - self.min_heap[0] <= -self.max_heap[0] - num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if len(self.min_heap) == len(self.max_heap) + 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) == len(self.min_heap) + 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
    def findMedian(self) -> float:
        """O(1)"""
        n1, n2 = len(self.min_heap), len(self.max_heap)
        if n1 < n2:
            left = right = -self.max_heap[0]
        elif n2 < n1:
            left = right = self.min_heap[0]
        else:
            left, right = -self.max_heap[0], self.min_heap[0]
        return (left + right) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    for MedianFinder in [MedianFinder1, MedianFinder2]:
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        assert medianFinder.findMedian() == 1.0
        medianFinder.addNum(2)
        assert medianFinder.findMedian() == 1.5
        medianFinder.addNum(3)
        assert medianFinder.findMedian() == 2.0
        medianFinder.addNum(4)
        assert medianFinder.findMedian() == 2.5
        medianFinder.addNum(5)
        assert medianFinder.findMedian() == 3.0
        medianFinder.addNum(6)
        assert medianFinder.findMedian() == 3.5
        medianFinder.addNum(7)
        assert medianFinder.findMedian() == 4.0
        medianFinder.addNum(4.5)
        assert medianFinder.findMedian() == 4.25
    
        medianFinder = MedianFinder()
        medianFinder.addNum(5)
        assert medianFinder.findMedian() == 5.0
        medianFinder.addNum(4)
        assert medianFinder.findMedian() == 4.5
        medianFinder.addNum(3)
        assert medianFinder.findMedian() == 4.0
        medianFinder.addNum(2)
        assert medianFinder.findMedian() == 3.5
        medianFinder.addNum(1)
        assert medianFinder.findMedian() == 3.0
    
        medianFinder = MedianFinder()
        medianFinder.addNum(-1)
        assert medianFinder.findMedian() == -1.0
        medianFinder.addNum(-2)
        assert medianFinder.findMedian() == -1.5
        medianFinder.addNum(-3)
        assert medianFinder.findMedian() == -2.0
        medianFinder.addNum(-4)
        assert medianFinder.findMedian() == -2.5
        medianFinder.addNum(-5)
        assert medianFinder.findMedian() == -3.0
