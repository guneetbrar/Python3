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
    Divide the number of flyers evenly among volunteers to 
    advertise for a charity event
    Use: flyers_given = flyers // volunteers
         flyers_left = flyers % volunteers
    -------------------------------------------------------
    Parameters:
        flyers - number of flyers to be distributed (int)
        volunteers - number of volunteers (int)
    Returns:
         flyers_given - flyers to be distributed (int)
         flyers_left - flyers left (int)
    ------------------------------------------------------
    """
# Input
flyers = int(input('Number of flyers: '))
volunteers = int(input('Number of volunteers: '))

# Processing
flyers_given = flyers // volunteers
flyers_left = flyers % volunteers

# Print
print('Each volunteer will receive {} flyer/s'.format(flyers_given))
print('flyers that will not be distributed: {}'.format(flyers_left))