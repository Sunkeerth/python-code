"""
/*
============================================================
ARRAY MERGER
============================================================

DESCRIPTION:
Given two sorted arrays, merge them into one sorted array.

INPUT:
N
First sorted array
M
Second sorted array

OUTPUT:
Merged array in sorted order.

EXAMPLE:

Input:
3
1 2 3
4
4 5 6 7

Output:
Merged array: 1 2 3 4 5 6 7

CONSTRAINT:
1 <= N, M <= 10^5

APPROACH:
Use TWO POINTERS.

i -> points to first array
j -> points to second array

Compare arr1[i] and arr2[j].
Take the smaller element and move that pointer.

After one array finishes, add the remaining elements
of the other array.

TIME COMPLEXITY:
O(N + M)

SPACE COMPLEXITY:
O(N + M)

KEY CONCEPT:
Sorted Arrays + Two Pointers
============================================================
*/
000"""

n=int(input("enter the n value : "))
n1=int(input("enter the n1 value : "))

arr=list(map(int,input("enter the array 0  values : ").strip().split()))
arr1=list(map(int,input("enter the array 1  values : ").strip().split()))

# case 1 : output : 
"""
enter the n value : 3
enter the n1 value : 4
enter the array 0  values : 1 2 3
enter the array 1  values : 4 5 6 7
[[1, 2, 3], [4, 5, 6, 7]]
"""
# def merge_sorted_arrays(arr, arr1):
#     sorted_array=[]
#     sorted_array.append(arr)
#     sorted_array.append(arr1)
#     print(sorted_array)
# merge_sorted_arrays(arr, arr1)

def merge_sorted_arrays(arr, arr1):
    sorted_array=[]
    i=0
    j=0
    while i<n and j<n1:
        if arr[i]<arr1[j]:
            sorted_array.append(arr[i])
            i+=1
        else:
            sorted_array.append(arr1[j])
            j+=1
    sorted_array.extend(arr[i:])
    sorted_array.extend(arr1[j:])
    print("Merged array:", sorted_array)
merge_sorted_arrays(arr,arr1)



    


