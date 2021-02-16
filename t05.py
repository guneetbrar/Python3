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
    Program outputs the weighted exam mark 
    (as a percentage value) of midterm-mark and final exam
    marks
    Use: exam_portion = ((0.2 * midterm_test_mark) + 
        (0.4 * final_test_mark)) / (0.2 + 0.4)
    -------------------------------------------------------
    Parameters:
        midterm_test_mark - input mid term marks (int)
        final_test_mark - input final term marks (int)
    Returns:
         exma_portion - outputs the weighted exam average (float)
    ------------------------------------------------------
    """
# Input
midterm_test_mark = int(input('Midterm mark (%): '))
final_test_mark = int(input('Final mark (%): '))

# Processing
exam_portion = ((0.2 * midterm_test_mark) + (0.4 * final_test_mark)) / (0.2 + 0.4)

# Print 
print('Your weighted exam average is: {:.1f} %. The passing mark of the weighted exam average is 50%'.format(exam_portion))