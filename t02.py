"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Guneet Singh
ID:      211605090
Email:   sing0509@mylaurier.ca
__updated__ = "2021-02-06"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    Ask the user to enter a positive two-digit integer num_2d.
    The program outputs the sum of the two digits
    Use: num_one = num_2d // 10
         num_two = num_2d % 10
         total = num_one + num_two
    -------------------------------------------------------
    Parameters:
        num_2d - Two digit positive integer (int)
    Returns:
         total - sum of the first and the second digit (int)
    ------------------------------------------------------
    """
# Input
num_2d = int(input('Enter a positive two-digit integer: '))

# Processing
num_one = num_2d // 10
num_two = num_2d % 10
total = num_one + num_two

# Print
print('The total is: {}'.format(total))
