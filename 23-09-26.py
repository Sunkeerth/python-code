"""

============================================================
ARRAY MERGER (THREE ARRAYS)
============================================================

PROBLEM:
--------
Merge three arrays into a single array.

INPUT:
------
The input consists of:

1. Size of the first array
2. Elements of the first array
3. Size of the second array
4. Elements of the second array
5. Size of the third array
6. Elements of the third array

OUTPUT:
-------
Print the merged array elements in a single line,
separated by spaces.


============================================================
SOLUTION:
============================================================

Read all three arrays and combine them into one array.

The order of elements should remain the same as they
appear in the input arrays.

Python approach:
    merged = arr1 + arr2 + arr3


============================================================
TEST CASE 1
============================================================

INPUT:
3
1 2 3
4
4 5 6 7
2
8 9

OUTPUT:
1 2 3 4 5 6 7 8 9


============================================================
TEST CASE 2
============================================================

INPUT:
2
5 2
3
1 5 2
4
3 2 5 4

OUTPUT:
5 2 1 5 2 3 2 5 4


============================================================
KEY IDEA:
============================================================

Merge three arrays using:

merged = arr1 + arr2 + arr3

The original order of elements is preserved.

============================================================
"""

n= int(input("Enter the size of the first array: "))
n1= int(input("Enter the size of the second array: "))
n2= int(input("Enter the size of the third array: "))
arr=list(map(int, input("Enter the elements of the first array: ").strip().split()))
arr1=list(map(int, input("Enter the elements of the second array: ").strip().split()))
arr2=list(map(int, input("Enter the elements of the third array: ").strip().split()))

# def merge_arrays(arr, arr1, arr2):
#     merged = arr + arr1 + arr2
#     return merged

# res=merge_arrays(arr, arr1, arr2)
# print("Merged array:", ' '.join(map(str, res)))

# def merge_arrays_sorted(arr, arr1, arr2):
#     i=j=k=0
#     merged=[]
#     while i<n and j<n1 and k<n2:
#         if arr[i]<arr1[j] and arr[i]<arr2[k]:
#             merged.append(arr[i])
#             i+=1
#         elif arr1[j]<arr2[k]:
#             merged.append(arr1[j])
#             j+=1
#         else:
#             merged.append(arr2[k])
#             k+=1
#     print("Merged array:", merged)
# merge_arrays_sorted(arr, arr1, arr2)

def array_sorted(arr,arr1,arr2):
    merged=[]
    merged.extend(arr)
    merged.extend(arr1)
    
    merged.extend(arr2)
    merged.sort()
    print("Merged array:", merged)

array_sorted(arr,arr1,arr2)