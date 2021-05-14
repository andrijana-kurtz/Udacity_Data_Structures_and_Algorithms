"""
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""


'''

i
l         h
2 0 2 1 0 1

i
l       h
1 0 2 1 0 2

  i
l       h
1 0 2 1 0 2

    i
  l     h
0 1 2 1 0 2

    i
  l   h
0 1 0 1 2 2

      i
    l h
0 0 1 1 2 2

      l i
      h
0 0 1 1 2 2
'''

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    i = 0
    l = 0 # keep 0 values before this pointer
    h = len(input_list)-1 # keep 2 values after this pointer

    while i <= h:
        if input_list[i] == 0:
            input_list[i], input_list[l] = input_list[l], input_list[i]
            i += 1
            l += 1
        elif input_list[i] == 1:
            i += 1
        else:
            input_list[i], input_list[h] = input_list[h], input_list[i]
            h -= 1

    return input_list
            
            
            
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0])
test_function([1])
test_function([2])
test_function([1, 0])
test_function([2, 1])
test_function([2, 0])
