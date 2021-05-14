"""
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

    min_i = None
    max_i = None

    for n in ints:
        if min_i is None and max_i is None:
            min_i = n
            max_i = n
            continue

        min_i = min_i if min_i < n else n
        max_i = max_i if max_i > n else n

    return min_i, max_i

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail") # edge case - empty input list


l = [i for i in range(0, 10000000)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((None, None) == get_min_max([])) else "Fail") # edge case - large input list