"""
PROBLEM STATEMENT: NUMBER ENDS WITH ZERO

Description:
Write a program to determine whether a given integer 'n' ends with the digit zero ('0').

Input Format:
The input consists of a single integer 'n' on a single line.

Output Format:
Output 'Yes' if the number ends with zero, otherwise output 'No'.

Constraints:
0 <= n <= 10^9

Sample Case 1:
Input:
140
Output:
Yes

Sample Case 2:
Input:
145
Output:
No """
n=int(input("enter the n : "))
# def ends_with_zero(n):
#     if n%10==0:
#         print("Yes")
#     else:
#         print("No")
# ends_with_zero(n)

"""
# ==========================================
# PROBLEM STATEMENT: Largest Number of Two
# ==========================================
# Write a program to find the largest number among two given integers.
#
# Input Format:
#   - The first line contains the first integer n.
#   - The second line contains the second integer m.
#
# Output Format:
#   - Print the largest number among the two input numbers.
#
# Constraints:
#   - Both integers are in the range of [-10^9, 10^9].
#
# Sample Case 1:
#   Input:
#     10
#     30
#   Output:
#     30
#
# Sample Case 2:
#   Input:
#     5
#     5
#   Output:
#     5
# ==========================================
"""
# m=int(input("enter the m : "))
# def largest_of_two(n,m):
#     if n>m:
#         print(n ," is the largest number")
#     else:
#         print(m," is the largest number"  )

# largest_of_two(n,m)

"""
# ==============================================================================
# PROBLEM STATEMENT: Sum of Digits
# ==============================================================================
# Description:
#   Find the sum of all digits in a positive integer.
#
# Input Format:
#   - A single positive integer num.
#
# Output Format:
#   - A single integer representing the sum of digits.
#
# Constraints:
#   - num is a positive integer with at most 10 digits (0 < num < 10^10).
#
# Sample Case 1:
#   Input:
#     987654
#   Output:
#     39
#
# Sample Case 2:
#   Input:
#     123456789
#   Output:
#     45
# ==============================================================================


"""
# sum=1
# def sum_of_integer(n):
#     sum=0
#     for i in n:
#         sum=sum+int(i)
#     return sum

# res=sum_of_integer(n)
# print("sum of integer is:",res)

# ==============================================================================
# PROBLEM STATEMENT: Factors
# ==============================================================================
# Description:
#   Write a program to find factors of a given number.
#
# Input Format:
#   - First line consists of a positive integer n.
#
# Output Format:
#   - Print the space separated integer factors of given number.
#
# Constraints:
#   - 1 <= n <= 10^6
#
# Sample Case 1:
#   Input:
#     20
#   Output:
#     1 2 4 5 10 20
#
# Sample Case 2:
#   Input:
#     15
#   Output:
#     1 3 5 15
# ========================================================================

def factors(n):
    fac_=[]
    for i in range(1,n+1):
        if n%i==0:
            fac_.append(i)
    return fac_

factors_of_n=factors(n)
print("factors of n are:",factors_of_n)