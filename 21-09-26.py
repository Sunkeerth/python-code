"""
============================================================
COUNT OCCURRENCES OF ALL ELEMENTS IN A SORTED ARRAY
============================================================

Difficulty: MEDIUM


DESCRIPTION
-----------

Count the number of occurrences for each unique element in a
sorted array.


INPUT FORMAT
------------

The input consists of two lines:-

The first line contains a single integer, N, representing the
size of the array (1 ≤ N ≤ 10^5).

The second line contains N space-separated integers,
A[1], A[2], ..., A[N], representing the elements of the array
(-10^9 ≤ A[i] ≤ 10^9).


OUTPUT FORMAT
-------------

Print N lines, each containing two space-separated integers:
X and Y.

X represents a unique element from the array, and Y represents
the number of times X occurs in the array.

The lines should be printed in ascending order of X.


============================================================
SAMPLE CASE 1
============================================================

INPUT:

8
1 2 3 3 4 4 4 5


OUTPUT:

1 1
2 1
3 2
4 3
5 1


EXPLANATION:

Element 1 occurs 1 time.
Element 2 occurs 1 time.
Element 3 occurs 2 times.
Element 4 occurs 3 times.
Element 5 occurs 1 time.


============================================================
SAMPLE CASE 2
============================================================

INPUT:

6
1 2 3 4 5 6


OUTPUT:

1 1
2 1
3 1
4 1
5 1
6 1


EXPLANATION:

Every element occurs exactly once.


============================================================
CONSTRAINTS
============================================================

1 ≤ N ≤ 10^5

-10^9 ≤ A[i] ≤ 10^9



============================================================
TIME COMPLEXITY
============================================================

Using the sorted-array approach:

Time Complexity: O(N)

Space Complexity: O(1)

Why?

The array is already sorted, so we do not need a dictionary
or sorting operation.

We simply move through the array once and count consecutive
equal elements.


============================================================
IMPORTANT IDEA
============================================================

Because the array is SORTED:

Example:

1 2 3 3 4 4 4 5

All equal elements are together.

Therefore:

1       -> count = 1
2       -> count = 1
3 3     -> count = 2
4 4 4   -> count = 3
5       -> count = 1

We can count each group of equal elements and then jump
directly to the next unique element.


============================================================
EXPECTED OUTPUT FORMAT
============================================================

For every unique element:

element frequency

Example:

3 2

means:

Element 3 occurs 2 times.


============================================================
KEY CONCEPT
============================================================

SORTED ARRAY + FREQUENCY COUNTING

Since the array is sorted, duplicate values occur
consecutively.

This allows us to solve the problem in O(N) time without
using an additional frequency dictionary.
============================================================
"""
n=int(input("Enter the size of the array:  "))
arr=list(map(int,input("Enter the elements of the array:  ").split()))

# def unique_pair(arr):
#     count=0
#     ele=arr[0]
#     n=len(arr)
#     for i in range(0,len(arr)):
#         if arr[i]==ele:
#             count+=1
#         else:
#             print(ele,count)
#             ele=arr[i]
#             count=1

# unique_pair(arr)

def count_occurrences(arr):
    # Start from the first element
    i = 0

    # Continue until we reach the end of the array
    while i < len(arr):

        # Store the current element
        element = arr[i]

        # Start counting this element
        count = 0

        # Count all consecutive occurrences
        while i < len(arr) and arr[i] == element:
            count += 1
            i += 1

        # Print the element and its frequency
        print(element, count)


# Call the function
count_occurrences(arr)
   