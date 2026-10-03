"""
============================================================
EVEN SUBARRAYS
============================================================

PROBLEM:
--------
Print all possible subarrays whose sum is even.

A subarray is a continuous part of the given array.


INPUT:
------
First line  : N (number of elements)
Second line : N space-separated integers


OUTPUT:
-------
Print all subarrays whose sum is even.
Print each subarray on a separate line.

If no such subarray exists, print:

None


============================================================
SAMPLE CASE 1
============================================================

INPUT:
5
1 2 3 4 5

OUTPUT:
2
4
1 2 3
3 4 5
1 2 3 4
2 3 4 5


============================================================
SAMPLE CASE 2
============================================================

INPUT:
4
-1 -2 -3 -4

OUTPUT:
-2
-4
-1 -2 -3
-1 -2 -3 -4


============================================================
CONSTRAINTS:
============================================================

1 <= N <= 20
-100 <= array element <= 100


============================================================
KEY IDEA:
============================================================

A subarray must be CONTINUOUS.

For every starting position:
    - Start sum = 0
    - Add elements one by one
    - If sum % 2 == 0, print the subarray

Example:

[1, 2, 3]

Subarrays:
[1]       → sum = 1  → odd
[1, 2]    → sum = 3  → odd
[1, 2, 3] → sum = 6  → even
[2]       → sum = 2  → even
[2, 3]    → sum = 5  → odd
[3]       → sum = 3  → odd


============================================================
"""

# n=int(input("Enter the size of the array: "))
# arr=list(map(int,input("Enter the elements of the array: ").strip().split()))

# def possible_sub_arrays(arr):
#     even_sum=0
#     res=[]
#     i=0
#     while i<len(arr):
#         if arr[i]%2==0:
#             print(arr[i])
#         j=i
#         while j<len(arr):
#             even_sum+=arr[j]
#             if even_sum%2==0:
#                 print(*res)
#             j+=1
#         i+=1
            
        
# possible_sub_arrays(arr)

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array: ").strip().split()))


def possible_sub_arrays(arr):

    i = 0

    while i < len(arr):

        even_sum = 0
        res = []

        j = i

        while j < len(arr):

            # Add current element
            res.append(arr[j])

            # Update sum
            even_sum += arr[j]

            # Check whether sum is even
            if even_sum % 2 == 0:
                print(*res)

            j += 1

        i += 1


possible_sub_arrays(arr)