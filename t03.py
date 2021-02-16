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
    Convert the date in the following format MMDDYYYY and 
    then display the date in the format DD/MM/YYYY
    Use: day = (input_date // 10000) % 100
         month = input_date // 1000000
         year = input_date % 10000
    -------------------------------------------------------
    Parameters:
        input_date - input date in the MMDDYYYY format (int)
    Returns:
         day - date extracted from MMDDYYYY (int)
         month - month extracted from MMDDYYYY (int)
         year - year extracted from MMDDYYYY (int)
    ------------------------------------------------------
    """
# Input
input_date = int(input('Enter a date in the format MMDDYYYY: '))

# Processing
day = (input_date // 10000) % 100
month = input_date // 1000000
year = input_date % 10000

# Print
print('{}/{}/{}'.format(day,month,year))
