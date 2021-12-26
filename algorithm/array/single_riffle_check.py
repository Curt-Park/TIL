"""
https://www.interviewcake.com/question/python3/single-riffle-check?course=fc1&section=array-and-string-manipulation

I figured out how to get rich: online poker.
I suspect the online poker game I'm playing shuffles cards by doing a single riffle.

To prove this, let's write a function to tell us if a full deck of cards 
shuffled_deck is a single riffle of two other halves half1 and half2.

We'll represent a stack of cards as a list of integers in the range 
1..52 (since there are 52 distinct cards in a deck).

Why do I care? A single riffle is not a completely random shuffle. 
If I'm right, I can make more informed bets and get rich and finally 
prove to my ex that I am not a "loser with an unhealthy cake obsession" 
(even though it's too late now because she let me go and she's never getting me back).

A "riffle" is the standard way people shuffle cards by hand. You know, the thing that looks like this:

------

Here's a rigorous definition of the riffle algorithm:

1. cut the deck into halves half1 and half2
2. grab a random number of cards from the top of half1 
(could be 0, must be less than or equal to the number of cards left in half1) 
and throw them into the shuffled_deck
3. grab a random number of cards from the top of half2 
(could be 0, must be less than or equal to the number of cards left in half2) 
and throw them into the shuffled_deck
4. repeat steps 2-3 until half1 and half2 are empty.
"""

def is_riffled_once(shuffled_deck, half1, half2):
    """
    >>> is_riffled_once([], [], [])
    True
    >>> is_riffled_once([1, 2, 3, 4], [1, 2, 3, 4], [])
    True
    >>> is_riffled_once([1, 2, 3, 4], [], [1, 2, 3, 4])
    True
    >>> is_riffled_once([1, 2, 3, 4], [1, 2], [3, 4])
    True
    >>> is_riffled_once([1, 2, 3, 4], [1, 3], [2, 4])
    True
    >>> is_riffled_once([1, 2, 3, 4], [2, 1], [3, 4])
    False
    >>> is_riffled_once([1, 2, 3, 4], [1, 2, 5], [3, 4])
    False
    """
    n, n1, n2 = len(shuffled_deck), len(half1), len(half2)
    
    if n != n1 + n2:
        return False
    
    j, k = 0, 0
    for i in range(n):
        if j < n1 and shuffled_deck[i] == half1[j]:
            j += 1
        elif k < n2 and shuffled_deck[i] == half2[k]:
            k += 1
        else: 
            return False
            
    return True
        
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
