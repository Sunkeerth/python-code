# ==============================================================================
# PROBLEM STATEMENT: First Element Not In Sorting Order
# 
# Description:
# Find the first element in an array (intended to be sorted in ascending order) 
# that is not in the correct sorting order.
#
# Input Format:
# - Line 1: An integer 'n' (2 <= n <= 100), representing the size of the array.
# - Line 2: 'n' space-separated integers representing the elements of the array.
#
# Output Format:
# - Print the first element that is not in sorting order. 
# - If all elements are perfectly in sorting order, print -1.
#
# Constraints:
# - The array contains only integers.
# - 2 <= n <= 100
# - There will be at most one element that is not in sorting order.
#
# Sample Case 1:
#   Input:
#     7
#     1 2 3 6 4 5 7
#   Output:
#     4
#
# Sample Case 2:
#   Input:
#     5
#     1 2 3 4 5
#   Output:
#     -1
# ==============================================================================

n=int(input("enter the n vale size of array : "))
arr=list(map(int, input("enter the array values by space seprated : ").strip().split()))

def find_first_non_sorted_ele(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            print(arr[i])
            return

    print(-1)
        
find_first_non_sorted_ele(arr)