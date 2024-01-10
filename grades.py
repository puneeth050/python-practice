#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []

    for grade in grades:
        if grade < 38:
            # If grade is less than 38, no rounding occurs
            rounded_grades.append(grade)
        else:
            # Calculate the next multiple of 5
            next_multiple_of_5 = (grade // 5 + 1) * 5

            # Check if rounding is needed
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)

    return rounded_grades

# grades_count = int(input().strip())

grades = [4,73,67,38,33]

# for _ in range(grades_count):
#     grades_item = int(input().strip())
#     grades.append(grades_item)

result = gradingStudents(grades)
print(result)
