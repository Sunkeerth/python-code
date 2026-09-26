"""
============================================================
COMMON REPEATING ODD ELEMENTS IN SORTED ARRAYS
============================================================

PROBLEM:
--------
Find the common repeating odd elements in two sorted arrays.

INPUT:
------
1. Size of array A
2. Elements of array A
3. Size of array B
4. Elements of array B

OUTPUT:
-------
Print the odd elements that are common to both arrays,
in ascending order.

If no common odd elements are found, print:

No common odd elements found.


============================================================
TEST CASE 1
============================================================

INPUT:
5
1 2 3 4 5
5
3 4 5 6 7

OUTPUT:
3 5


============================================================
TEST CASE 2
============================================================

INPUT:
4
2 4 6 8
4
1 3 5 7

OUTPUT:
No common odd elements found.


============================================================
CONSTRAINTS:
============================================================

Length of arrays A and B <= 10^5

Elements of arrays A and B:
-10^9 to 10^9

============================================================
KEY IDEA:
============================================================

Both arrays are already sorted.

Find elements that:
1. Are present in both arrays.
2. Are odd numbers.

Example:

A = 1 2 3 4 5
B = 3 4 5 6 7

Common elements = 3, 4, 5

Odd common elements = 3, 5

Output:
3 5
============================================================
"""

n= int(input("enter the size of the first array: "))
arr= list(map(int, input("enter the elements of the first array: ").strip().split()))
n1= int(input("enter the size of the second array: "))
arr1= list(map(int, input("enter the elements of the second array: ").strip().split()))

def odd_common_ele(arr, arr1):
    
    common_odd_elements = []

    i = 0
    j = 0

    while i < len(arr) and j < len(arr1):

        # Common and odd element
        if arr[i] == arr1[j] and arr[i] % 2 != 0:
            common_odd_elements.append(arr[i])
            i += 1
            j += 1

        # First array element is smaller
        elif arr[i] < arr1[j]:
            i += 1

        # Second array element is smaller
        else:
            j += 1

    if common_odd_elements:
        print(*common_odd_elements)
    else:
        print("No common odd elements found")




odd_common_ele(arr, arr1)