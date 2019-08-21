"""
https://leetcode.com/problems/reconstruct-itinerary/

332. Reconstruct Itinerary
Medium

Given a list of airline tickets represented by pairs of departure and
arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order
than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
        ["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation:
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.
"""

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        >>> fn = Solution().findItinerary
        >>> fn([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
        ["JFK", "MUC", "LHR", "SFO", "SJC"]
        >>> fn([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
        ["JFK","ATL","JFK","SFO","ATL","SFO"]
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
