# Problem Statement:
# Write a program to find whether the given number is a prime number or not.
#
# Input Format:
# First line consists of a positive integer n
#
# Output Format:
# Print Yes if the number is prime, else print No
#
# Constraints:
# 1 <= n <= 10^6
#
# Sample Case 1:
# Input: 11
# Output: Yes
#
# Sample Case 2:
# Input: 15
# Output: No

# n = int(input("Enter a positive integer: "))
# def prime_check(n):
#     if n<1:
#         return "No"
#     for i in range(2,n):
#         if n%i==0:
#             return "No"
#     return "Yes"

# res=prime_check(n)
# print(res)

# Problem Statement:
# Print all prime numbers from 2 up to and including 'n'.
#
# Input Format:
# The input is provided as a single integer 'n'.
#
# Output Format:
# The function should print the prime numbers on a single line, 
# each number separated by a space.
#
# Constraints:
# The value of 'n' is at least 2.
#
# Sample Case 1:
# Input: 2
# Output: 2
#
# Sample Case 2:
# Input: 15
# Output: 2 3 5 7 11 13

# def print_primes(n):
#     prime=[]
#     for i in range(2,n+1):
#         is_prime=True
#         for j in range(2,int(i**0.5)+1):# so the loop will run only till the square root of i 
#             """ if example i is 2 then int(2**0.5+1 is 2 so loppwill be empty then it is added to prime). 
#             i=4 then int(4**0.5+1=3) so loop will run for j=2 and 4%2==0 so is_prime=False and it will not be added to prime list"""
#             if i%j==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             prime.append(i)
#     return prime

# res=print_primes(n)
# print(*res)
# ==============================================================================

# Problem Statement:
# Write a program to find the greatest common factor of given 2 integers.
#
# Input Format:
# First line contains space separated integer input n, m.
#
# Output Format:
# Print greatest common factor of 2 numbers.
#
# Constraints:
# 1 <= n, m <= 10^6
#
# Sample Case 1:
# Input: 10 20
# Output: 10
#
# Sample Case 2:
# Input: 15 30
# Output: 15

""" if do reverse the number go with garest commend factor of 2 numbers 
"""

# Euclidean algorithm by repeated subtraction.

# n1=int(input("Enter first positive integer: "))
# n2=int(input("Enter second positive integer: "))
# def gcd_subtraction(n1,n2):
#     while n2!=0:
#         if n1>n2:
#             n1=n1-n2
#         else:
#             n2=n2-n1
#     return n1

# res=gcd_subtraction(n1,n2)
# print(res)

n1, n2=map(int ,input().strip().split())
# # print(n1,n2)

# def gdc_optimized(n1,n2):
#     while n2!=0:
#         n1,n2=n2,n1%n2
#     return n1
# res=gdc_optimized(n1,n2)
# print(res)

# """ prime numbers between n1 and n2"""
# def prime_no(n1,n2):
#     arr=[]
#     if n1<2 and n2<2:
#         return False
#     for i in range(n1,n2+1):
#         is_true=True
#         for j in range(n1,int(i**0.5)+1):
#             arr.append(i)

# res=prime_no(n1,n2)
# print(res)

def prime_no(n1, n2):

    arr = []

    if n2 < 2:
        return arr

    for i in range(max(n1, 2), n2 + 1):

        is_true = True

        for j in range(2, int(i ** 0.5) + 1):

            if i % j == 0:
                is_true = False
                break

        if is_true:
            arr.append(i)

    return arr



res = prime_no(n1, n2)

# n1=12,n2=13 

print(res)



