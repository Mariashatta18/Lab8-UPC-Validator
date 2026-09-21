"""
Program Name: UPC Validator
Author: Maria Shatta
Purpose: This program checks whether a 12-digit UPC-A code is valid by calculating
the expected check digit and comparing it with the check digit entered by the user.
Starter Code: No starter code was used.
Date: September 21, 2026
"""
def find_UPC(first_eleven):
    odd_sum = 0
    even_sum = 0

    for i in range(11):
        digit = int(first_eleven[i])

        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    total = (odd_sum * 3) + even_sum
    check_digit = (10 - (total % 10)) % 10

    return check_digit
