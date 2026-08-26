# Problem Statement:
# Given an array of integers of size N, find and display the smallest element present in the array.
#
# Input Format:
# The first line contains an integer N, the size of the array.
# The second line contains N space-separated integers representing the array elements.
#
# Output Format:
# Print the smallest element present in the array.
#
# Sample Case 1
# Input:
# 5
# 1 5 7 3 2
# Output:
# 1
#
# Sample Case 2
# Input:
# 6
# 0 -1 -2 -3 -4 -5
# Output:
# -5
#
# Constraints:
# 1 <= N <= 10^5
# -10^9 <= Array Elements <= 10^9

n=int(input("enter the n value as input :  "))
arr=list(map(int,(input("enter the array values with space seprated : ").strip().split())))
# print(arr)
# def smallest_ele(arr):
#     # easy
#     # arr.sort()
#     # print(arr[0])

#     #more easy 
#     print(min(arr))

# smallest_ele(arr)

"""
# Problem Statement:
# Write a program to find the sum of all elements present in an array.
#
# Input Format:
# First line contains a single integer N. Next line contains N space separated integer values.
#
# Output Format:
# Print sum of all elements in an array.
#
# Sample Case 1
# Input:
# 5
# 1 4 6 3 10
# Output:
# 24
#
# Sample Case 2
# Input:
# 6
# 1 2 3 4 5 6
# Output:
# 21
"""
# def sum_of_array(arr):
#     sum=0
#     for i in arr:
#         sum=sum+i
#     print(sum)
# sum_of_array(arr)

"""
Problem Statement:
# Print elements of the array from the middle to the end. """

def ele_mid_end(arr,n):
    mid=n//2
    print()
    for i in range(mid,n):
        print(arr[i],sep=' ',end=' ')
        
ele_mid_end(arr,n)