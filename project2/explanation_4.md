Efficiency: There is a clear and accurate statement of efficiency in time and space. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

Time eff: O(n)
We have to explore all the Groups and associated users in Active Directory

Space eff: O(g)
No additional data structures were used in is_user_in_group function, however we are adding stack frame each time we want to explore a group (recursive call), hence I claim that Space efficiency is O(g) where g is total number of groups in active directory 'tree'.


Code Design: Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.
Solution uses recursion to explore active directory 'tree'.

Readability: Explanation is written with proper English. Wording is clear and easy to understand. It’s okay to make a couple mistakes, but thoughts should be clearly expressed overall.
