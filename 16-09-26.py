"""
PAIRS WITH DIFFERENCE K

PROBLEM STATEMENT

Given an array of N integers and an integer K, find and print all pairs of numbers in the array whose absolute difference is equal to the given target difference K.

For every pair (arr[i], arr[j]) where i < j, calculate:

    |arr[i] - arr[j]| = K

If the absolute difference is equal to K, print both elements separated by a space.

Print each pair only once, in the order in which it is found.

INPUT FORMAT

The first line contains an integer N, representing the length of the array.

The second line contains N space-separated integers, representing the array elements.

The third line contains a single integer K, representing the target difference.

OUTPUT FORMAT

Print each pair of numbers whose absolute difference is equal to K on a new line, separated by a space.

CONSTRAINTS

0 < N <= 1000
0 < Array Elements <= 1000
0 < K <= 1000

SAMPLE CASE 1

Input:
5
3 1 5 4 2
2

Output:
3 1
3 5
4 2

EXPLANATION

The target difference is K = 2.

|3 - 1| = 2, so print 3 1.
|3 - 5| = 2, so print 3 5.
|4 - 2| = 2, so print 4 2.

SAMPLE CASE 2

Input:
6
8 12 5 9 15 6
3

Output:
8 5
12 9
12 15
9 6

EXPLANATION

The following pairs have an absolute difference of 3:

|8 - 5| = 3
|12 - 9| = 3
|12 - 15| = 3
|9 - 6| = 3

SOLUTION APPROACH

Use two nested loops to check every possible pair.

1. Read N, the array, and K.
2. Select the first element using an outer loop.
3. Select the second element using an inner loop starting at i + 1.
4. Calculate abs(arr[i] - arr[j]).
5. If the result equals K, print the pair.

TIME COMPLEXITY

O(N^2)

SPACE COMPLEXITY

O(1)
"""


n=int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").strip().split()))
k = int(input("Enter the target difference: "))

def find_pairs_with_difference(arr, k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] - arr[j] == k:
                print(arr[i], arr[j])
                
            elif arr[j] - arr[i] == k:
                print(arr[j], arr[i])
find_pairs_with_difference(arr, k)