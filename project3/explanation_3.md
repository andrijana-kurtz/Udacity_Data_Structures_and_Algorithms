Efficiency
There is a clear and accurate statement of efficiency. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

- Time efficiency is O(nlog(n)) since dominating algorithm used is merge sort.
- Space efficiency - Merge sort uses additional space in size of given input so it would be O(2n) which is still O(n) in the end


Code Design
Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.

- In order to construct two numbers I decided to first sort given input list. I've used merge sort algorithm provided by udacity lectures.
Once input was sorted, I've constructed two numbers by taking odd and even numbers for each and multiplying with appropriate positional unit value.
