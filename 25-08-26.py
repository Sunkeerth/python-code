# Problem: Common Factors of n and m (EASY)
# 
# Print the common factors of two positive integers n and m.
# 
# Input Format:
# Two positive integers n and m separated by a space.
# 
# Output Format:
# Common factors separated by a space.
# 
# Sample Case 1
# Input:
# 10 25
# Output:
# 1 5
# 
# Sample Case 2
# Input:
# 8 12
# Output:
# 1 2 4
# 
# Constraints:
# • n and m are positive integers.

# n,m=map(int,(input("enter the value n and m : ").strip().split()))
# # print(n,m)
# m1=max(n,m)
# mi=min(n,m)

# def common_factor(n,m):
#     factor=[]
#     for i in range(1,m1+1):
#         if n%i==0 and m%i==0:
#             # print(i," ")
#             factor.append(str(i))
#     print(" ".join(factor))


# common_factor(n,m)     
# 

# Problem: Even Numbers Array (EASY)
# 
# Write a program to print even numbers present in an array.
# 
# Input Format:
# First line contains a single integer N. 
# Next line contains N space separated integer values.
# 
# Output Format:
# Print space separated even integer values in an array.
# 
# Sample Case 1
# Input:
# 5
# 1 4 6 3 10
# Output:
# 4 6 10
# 
# Sample Case 2
# Input:
# 4
# 20 30 40 50
# Output:
# 20 30 40 50
# 
# Constraints:
# • 1 <= N <= 10^3
# • -10^6 <= array elements <= 10^6


n=int(input("enter the n value : "))
arr = list(map(int, input(" enter the space seprated values :").strip().split()))

# def even(arr):
#     even=[]
#     odd=[]
#     for i in arr:
#         if i%2==0:
#             even.append(i)
#         else :
#             odd.append(i)
#     print("even :", even)
#     print("odd  :", odd)
# even(arr)
     

# ==============================================================================
# PROBLEM STATEMENT: Average of Array (EASY)
# Write a program to find the average of all elements present in an array.
#
# INPUT FORMAT:
# - First line contains a single integer N.
# - Next line contains N space separated integer values.
#
# OUTPUT FORMAT:
# - Print float value of average of all elements in an array. 
# - [it has to print 2 decimal points]
#
# CONSTRAINTS:
# - 1 <= N <= 10^3
# - -10^6 <= array elements <= 10^6
#
# SAMPLE CASE 1:
# Input:
# 5
# 1 4 6 3 10
# Output:
# 4.80
#
# SAMPLE CASE 2:
# Input:
# 5
# 5 -10 -15 20 -25
# Output:
# -5.00
# 

def avg_of_array(arr):
    # total = sum(arr)
    # avg = total / len(arr)
    # print(f"{avg:.2f}")
    sum=0
    for i in arr:
        sum=sum+i
    avg1=sum/n
    print(f'{avg1:.2f}')


avg_of_array(arr)

# sum=1
# for i in arr:
#     sum=sum+i
# print(sum)







