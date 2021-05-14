from math import floor

'''
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))'''

def sqrt(number, guess=1):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    # check if input number is 0 return square as 0
    if number == 0:
        return 0

    # check if guess is good enough - base case
    if abs((guess * guess) - number) < 0.1:
        return floor(guess)

    return sqrt(number, ((guess + (number / guess)) / 2))

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (12 == sqrt(144)) else "Fail")
print ("Pass" if  (22 == sqrt(512)) else "Fail")


print ("Pass" if  (None == sqrt(-1)) else "Fail") # Test edge case - negative number input
print ("Pass" if  (300000 == sqrt(90000000000)) else "Fail") # Test edge case - large input number
