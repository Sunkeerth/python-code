"""
PAIRS WITH SUM GREATER THAN K

PROBLEM STATEMENT

Given an array of N integers and an integer K, print all possible pairs of numbers from the input array whose sum is greater than the given sum value K.

A pair consists of two different elements from the array. For every pair (arr[i], arr[j]) where i < j, check whether:

    arr[i] + arr[j] > K

If the condition is satisfied, print both elements of the pair separated by a space.

The pairs must be printed in the order in which they are found while traversing the array from left to right. Each pair should be printed only once.

INPUT FORMAT

The first line contains an integer N, representing the size of the array.

The second line contains N space-separated integers, representing the elements of the array.

The third line contains a single integer K, representing the target sum value.

OUTPUT FORMAT

Print each pair of numbers whose sum is greater than K on a new line, separated by a space.

The pairs must be printed in the order in which they are found while traversing the array from left to right.

CONSTRAINTS

1 <= N <= 1000
-10^9 <= arr[i] <= 10^9
-10^9 <= K <= 10^9

Each pair must contain two distinct array elements.

SAMPLE CASE 1

Input:
6
2 4 6 3 8 9
7

Output:
2 6
2 8
2 9
4 6
4 8
4 9
6 3
6 8
6 9
3 8
3 9
8 9

EXPLANATION

The given array is 2 4 6 3 8 9 and the target value is K = 7.

We check every possible pair of elements. If the sum of the two elements is strictly greater than 7, the pair is printed.

For example:
2 + 6 = 8, so print 2 6.
2 + 4 = 6, so do not print.
4 + 3 = 7, so do not print because the sum is equal to K.
8 + 9 = 17, so print 8 9.

SAMPLE CASE 2

Input:
4
1 2 3 4
6

Output:
3 4

EXPLANATION

The target value is K = 6.

3 + 4 = 7, which is greater than 6, so the pair 3 4 is printed.

The pair 2 4 has a sum of 6, which is equal to K, so it is not printed.

SOLUTION APPROACH

Use two nested loops to generate every possible pair of elements.

1. Read the size of the array N.
2. Read the N array elements.
3. Read the target value K.
4. Use an outer loop to select the first element.
5. Use an inner loop starting from i + 1 to select the second element.
6. Calculate the sum of the selected pair.
7. If the sum is greater than K, print the pair.
8. Continue until all possible pairs have been checked.

TIME COMPLEXITY

O(N^2)

SPACE COMPLEXITY

O(1)"""

n= int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the space-separated values of the array: ").strip().split()))
k= int(input("Enter the target sum value K: "))

# def sum_of_k_pairs(arr,k):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] > k:
#                 print(arr[i], arr[j])
                
def sum_of_k_pairs(arr,k):
    for i in arr:
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] > k:
                print(arr[i], arr[j])

sum_of_k_pairs(arr,k)
