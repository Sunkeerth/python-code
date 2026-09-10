# ==========================================
# PROBLEM STATEMENT: Print All Pairs
# ENVIRONMENT: VS Code (Python 3)
# ==========================================
# Description:
# Print all possible unique pairs of numbers from a given array in the order they appear.
#
# Input Format:
# - First line contains a single integer N, representing the size of the array.
# - Second line contains N space-separated integers.
#
# Output Format:
# - Print each pair of numbers on a new line, separated by a single space.
#
# Constraints:
# - 0 < N <= 1000
# - -1000 <= Array Elements <= 1000
# ==========================================
# SAMPLE CASES
# ==========================================
# Sample Case 1 Input:
# 4
# 1 2 3 4
#
# Sample Case 1 Output:
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
#
# Sample Case 2 Input:
# 3
# -1 0 1
#
# Sample Case 2 Output:
# -1 0
# -1 1
# 0 1
# ==========================================
# SOLUTION CODE
# ==========================================

n =int(input("enter the n number : "))
arr=list(map(int, input("enter the array elements : ").strip().split()))

def print_arr_paris(arr):
    for i in arr:
        for j in arr[arr.index(i)+1::]:#slicing where j will go till last elemet cause its an step 1 
            print(i,j)
            
print_arr_paris(arr)
