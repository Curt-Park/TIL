"""
https://www.interviewcake.com/question/python3/inflight-entertainment?course=fc1&section=hashing-and-hash-tables

You've built an inflight entertainment system with on-demand movie streaming.
Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""

from typing import List


def watch_two_movies(flight_length: int, movie_lengths:List[int]) -> bool:
    """
    >>> watch_two_movies(-1, [5, 6])
    False
    >>> watch_two_movies(10, [5, 5, 6])
    True
    >>> watch_two_movies(10, [5, 6])
    False
    >>> watch_two_movies(10, [5, 6, -1])
    False
    >>> watch_two_movies(5, [5, 6, -1])
    False
    """
    
    if flight_length < 0 and not movie_lengths:
        return False
        
    s = set()
    
    for ml in movie_lengths:
        if ml < 0:
            return False
            
        remaining_time = flight_length - ml
        
        if remaining_time in s:
            return True
            
        s.add(ml)
        
    return False


def watch_two_movies2(flight_length: int, movie_lengths:List[int]) -> bool:
    """
    >>> watch_two_movies2(-1, [5, 6])
    False
    >>> watch_two_movies2(10, [5, 5, 6])
    True
    >>> watch_two_movies2(10, [5, 6])
    False
    >>> watch_two_movies2(10, [5, 6, -1])
    False
    >>> watch_two_movies2(5, [5, 6, -1])
    False
    """
    
    if flight_length < 0 and not movie_lengths:
        return False
    
    n = len(movie_lengths)
    ml_tab = {}
    
    for i in range(n):
        ml = movie_lengths[i]
        
        if ml < 0:
            return False
        
        if not ml in ml_tab:
            ml_tab[ml] = 1
        else:
            ml_tab[ml] += 1
    
    for ml in ml_tab:
        ml_tab[ml] -= 1
        remaining_time = flight_length - ml
        
        if remaining_time in ml_tab and ml_tab[remaining_time] > 0:
            return True
            
        ml_tab[ml] += 1
            
    return False
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
