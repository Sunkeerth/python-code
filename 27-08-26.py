"""
Problem Statement:
Write a program that finds the maximum sum among all the pairs of elements in a 
given array of integers without sorting.

Input Format:
- The first line contains a single integer, N, representing the size of the array.
- The second line contains N space-separated integers, representing the elements of the array.

Output Format:
- Print the maximum sum among all the pairs of elements in the array.

Sample Case 1:
Input:
6
5 9 2 8 3 7
Output:
17

Sample Case 2:
Input:
7
10 5 8 2 6 1 4
Output:
18
"""
n=int(input("enter n value :"))
arr=list(map(int,(input("enter the array values by space seprated :  ").strip().split())))
# print(arr)

# def max_sum_array_ele(arr):
#     # st_ele=arr[0]
#     # se_ele=arr[1]
#     # sum_ele=st_ele+se_ele
#     # for i in range(1,n+1):
#     #     if arr[i]
#     sorted_ele=sorted(arr)
#     print(sorted_ele)
#     max_elemest=0
#     """enter n value :5
# enter the array values by space seprated :  12 13 14 15 18 
# [12, 13, 14, 15, 18]
# 18 15"""
#     for i in range(-1,0):
#         print(sorted_ele[i],sorted_ele[i-1])
#         max_elemest=sorted_ele[i]+sorted_ele[i-1]
#     print(max_elemest," : max_element sum ")




    


# max_sum_array_ele(arr)


"""
**
 * PROBLEM: Minimum Pairs Sum (Medium)
 * 
 * Description:
 * This program finds the minimum sum among all pairs of elements in a given
 * array of integers.
 * 
 * CRITICAL CONSTRAINT:
 * Sorting is strictly NOT allowed.
 * 
 * Constraints:
 * - 2 <= N <= 10^5 (size of the array)
 * - -10^9 <= elements <= 10^9
 * 
 * Complexity:
 * - Time Complexity: O(N) -> Single pass traversal
 * - Space Complexity: O(1) -> Memory usage remains constant
 */"""

def min_sum_ele(arr):
    min1 =min2=float('inf')
    max1 =max2 =float('-inf')

    for i in arr:
        if i <min1:
            min2=min1
            min1=i
        elif i<min2:
            min2=i
    print(min1,"  :  ",min2)
    sum_min=min1+min2
    print("mini sum of array : ",sum_min)
min_sum_ele(arr)