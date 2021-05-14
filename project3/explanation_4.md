Efficiency
There is a clear and accurate statement of efficiency. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

- Time efficiency is O(n)
- Space efficiency - 0(n) if we count given input, otherwise it's O(1)


Code Design
Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.

- Famous CS problem -> https://en.wikipedia.org/wiki/Dutch_national_flag_problem, algorithm uses property of input, that there is only three distinct elements; 0, 1 and 2. We have three pointers, 'i' is used to iterate through given input, and we shift all 0 values before pointer 'l', 1 values between pointers 'l' and 'h' and 2 values after pointer 'h'.
