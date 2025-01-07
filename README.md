# Python code error: TypeError in average calculation

This repository demonstrates a common error in Python: a `TypeError` occurring when the `sum()` function encounters a non-numeric element in a list. The `calculate_average` function is designed to calculate the average of a list of numbers. However, it fails when the input list contains non-numeric data.

The `bug.py` file contains the erroneous code, while `bugSolution.py` demonstrates the improved solution to address this error. 

## Bug:
The original code lacks error handling for non-numeric elements in the input list.  This leads to a `TypeError` during execution if the list contains any strings or other non-numeric types.

## Solution:
The solution includes type checking within the function to ensure that all elements in the list are numeric before performing calculations. This prevents the `TypeError` and makes the function more robust.