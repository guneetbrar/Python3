"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Guneet Singh
ID:      211605090
Email:   sing0509@mylaurier.ca
__updated__ = "2021-01-23"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """

# Input
principal = int(input('Principal: '))
interest = float(input('Interest (decimal): '))
years = int(input('Number of years: '))
compound_interest = int(input('Compound interest per year: '))

# Processing
balance = principal * (1.0 + (interest/compound_interest))**(compound_interest*years)

#Output
print('Balance: ${:.2f}'.format(balance))
