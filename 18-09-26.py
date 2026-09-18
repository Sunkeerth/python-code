# Problem: First Element Not In Sorting Order
# Difficulty: Easy
#
# Description:
# Find the first element in a sorted array that is not in sorting order.
#
# Input Format:
# The input consists of two lines:
# - The first line contains an integer 'n' (2 <= n <= 100), representing the size of the array.
# - The second line contains 'n' space-separated integers, 'arr[0]' to 'arr[n-1]', representing the elements of the array.
#
# Output Format:
# Print the first element that is not in sorting order. If all elements are in sorting order, print -1.
#
# Sample Case 1:
# Input:
# 7
# 1 2 3 6 4 5 7
# Output:
# 4
#
# Sample Case 2:
# Input:
# 5
# 1 2 3 4 5
# Output:
# -1
#
# Constraints:
# - The array will be sorted in ascending order.
# - The array will contain only integers.
# - The size of the array will be at least 2 and at most 100.
# - There will be at most one element that is not in sorting order.

n= int(input("enter the n value : "))
arr=list(map(int, input("Enter the array values space seprated values : ").strip().split()))

def first_element_not_in_order(arr):
    for i in range(1,len(arr)):
        if arr[i]>arr[i+1]:
            return arr[i+1]
    return -1

result=first_element_not_in_order(arr)
print(result)

  
