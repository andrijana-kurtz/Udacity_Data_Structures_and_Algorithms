Efficiency
There is a clear and accurate statement of efficiency. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

- Time efficiency is O(log(n)) - using binary search around pivot point 
- Space efficiency is O(1) - constant number (non n) of vars used to keep high low mid positions for search


Code Design
Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.

Algorithm outline:
  - check if pivot point is number we are looking for
  - if not, identify if we need to execute binary search on left or right side subarry
  - perform binary search 
