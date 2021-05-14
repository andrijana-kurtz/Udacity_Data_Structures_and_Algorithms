Efficiency
There is a clear and accurate statement of efficiency. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

- Time efficiency is O(log(n)) as a result of nature of used algorithm - Newton's Method, which in it's essence is improving 'guess' by halfing it in each iteration.
- Space efficiency - constant number of variables were used to store data additional to given input


Code Design
Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.

- I used Newton's method to find squre roots, source of information was: https://en.wikipedia.org/wiki/Newton%27s_method and SICP.
Function sqrt recurses while trying to find guess within acceptable margin of error (I chose 0.1 since problem asks us to floor end result anyway) for square root. 
