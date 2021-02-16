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
PROFIT_PERCENTAGE = 0.17

def func():
    """
    -------------------------------------------------------
    Enter the amount of total sales,and then display the 
    profit that will be made from that amount
    Use: profit = total_sales * PROFIT_PERCENTAGE
    -------------------------------------------------------
    Parameters:
        total_sales - amount of total sales (float > 0)
    Returns:
         profit - total amount of profit calculated (float > 0)
    ------------------------------------------------------
    """
# Input
total_sales = float(input('Enter the amount of total sales: $'))

# Processing
profit = total_sales * PROFIT_PERCENTAGE

# Print
print('Projected Profit Report')
print('--------------------------')
print('Total sales: ${:.2f}'.format(total_sales))
print('Annual profit: %17')
print('--------------------------')
print('Profit: ${:.2f}'.format(profit))


