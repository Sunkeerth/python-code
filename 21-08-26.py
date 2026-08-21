"""
Problem Statement:
Write a program to calculate the circumference of a circle. 
Formula: Circumference = 2 * pi * radius, where pi = 3.142

Input Format:
- First line contains an Integer representing the radius of a circle.

Output Format:
- Print the circumference of the circle formatted to exactly four decimal places.

Constraints:
- 1 <= radius <= 1000

Sample Case 1:
- Input: 10
- Output: 62.8400

Sample Case 2:
- Input: 50
- Output: 314.2000
"""

# You can write your solution code below this line
n=int(input("enter the number : "))
# import math
# def circumference_of_the_circle(x):
#     # Formula: Circumference = 2 * pi * radius, where pi = 3.142
#     cic=math.pi*2*x
#     return cic
# obj=circumference_of_the_circle(n)
# # Print the circumference formatted to exactly four decimal places
# print(f"{obj:.4f}")

"""
Problem Statement:
Write a program to convert celsius to fahrenheit. 
Formula: fahrenheit = (celsius * 9 / 5) + 32

Input Format:
- First line contains a single integer representing the celsius value.

Output Format:
- Print the value after converting celsius to fahrenheit. 
- The output should be formatted to exactly 1 decimal place.

Constraints:
- -100 <= celsius <= 100

Sample Case 1:
- Input: 12
- Output: 53.6

Sample Case 2:
- Input: 20
- Output: 68.0
"""

# You can write your solution code below this line

# def cel_faf(x):
#     # Formula: fahrenheit = (celsius * 9 / 5) + 32
#     fah=(x*9/5)+32
#     return fah

# obj=cel_faf(n)
# # Print the value after converting celsius to fahrenheit formatted to exactly 1 decimal place
# print(f'{obj:.1f}')


""" 
Problem: Even or Odd

Description:
Check if a given number is an even number or an odd number.

Input Format:
The first line contains a single integer n.

Output Format:
Print "Yes" if it is an even number, else "No".

Constraints:
1 <= n <= 10^6

Sample Case 1:
Input: 12
Output: Yes

Sample Case 2:
Input: 15
Output: No
"""
# def evn_odd(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# res=evn_odd(n)
# if res==True:
#     print("even")
# else:
#     print("odd")

"""
Problem: Multiple of 5

Description:
Determine whether the given number is a multiple of 5 or not.

Input Format:
The input consists of a single integer 'n'.

Output Format:
Output 'Yes' if the number is a multiple of 5, otherwise output 'No'.

Constraints:
0 <= n <= 10^9

Sample Case 1:
Input: 24
Output: No

Sample Case 2:
Input: 30
Output: Yes
"""
# mul=int(input("enter the number u want multiple:"))
# def mult_ofnumber(n):
#     if n%mul==0:
#         print("True it an multiple of n", n, " multiple of ", mul)
#     else:
#         print("False it is not an multiple of n", n, " multiple of ", mul)

# mult_ofnumber(n)


""" 
Problem: Two Digit Number

Description:
Check whether the given number is a two-digit number or not.

Input Format:
The input consists of a single integer 'n'.

Output Format:
Output 'Yes' if the number is a two-digit number, otherwise output 'No'.

Constraints:
0 <= n <= 10^9

Sample Case 1:
Input: 14
Output: Yes

Sample Case 2:
Input: 30
Output: Yes
"""
# def two_dig(n):
#     if  n>9 and n<100:
#         print("Yes it is a two digit number")
#     else:
#         print("No it is not a two digit number")
# two_dig(n)

""" 
Problem: Three Digit Palindrome

Description:
Determine whether a given integer is a valid three-digit palindrome. 
A three-digit palindrome reads the same backwards as forwards (for example, 121 or 505). Single-digit or two-digit palindromes (like 7 or 44) do not qualify.

Input Format:
The input consists of a single integer 'n'.

Output Format:
Output 'Yes' if the number is a valid three-digit palindrome, otherwise output 'No'.

Constraints:
0 <= n <= 10^9

Sample Case 1:
Input: 121
Output: Yes

Sample Case 2:
Input: 45
Output: No

Sample Case 3:
Input: 343
Output: Yes

Sample Case 4:
Input: 123
Output: No
"""

# def three_digit_palindrome(n):
#     if n>99 and n<1000:
#         str_n=str(n)
#         if str_n==str_n[::-1]:
#             print("Yes it is a three digit palindrome")
#         else:
#             print("No it is not a three digit palindrome")
#     else:
#         print("No it is not a three digit palindrome")

# three_digit_palindrome(n)


"""
PROBLEM: Absolute Value

Description:
Write a program to find the absolute value of a given integer.

Input Format:
The input consists of a single integer, n.

Output Format:
Print the absolute value of the integer.

Constraints:
-10^9 <= n <= 10^9

Sample Case 1:
Input: -5
Output: 5

Sample Case 2:
Input: 12
Output: 12
"""
# def absv(n):
#     if n<0:
#         return -n
#     else :
#         return n

# print(absv(n))

# give me an moderate level problem statement with input and output format and constraints.
# Problem Statement:
# Write a program to determine if a given year is a leap year or not. A leap year is a year that is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 

