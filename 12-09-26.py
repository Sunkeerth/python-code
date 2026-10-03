"""
Common Repeating Odd Elements in Sorted Arrays
Problem Statement

Given two sorted integer arrays, find all the common odd elements that appear in both arrays.

The output should contain the common odd elements in ascending order, separated by spaces.

If no common odd elements are found, print:

No common odd elements found.

Input Format
First line contains an integer n, representing the size of array A.
Second line contains n space-separated integers representing array A.
Third line contains an integer m, representing the size of array B.
Fourth line contains m space-separated integers representing array B.
Output Format

Print a single line containing the odd elements common to both arrays in ascending order, separated by spaces.

If no common odd elements exist, print:

No common odd elements found."""

n= int(input("Enter the size of array A: "))
arr1 = list(map(int, input("Enter the space-separated values of array A: ").strip().split()))
m= int(input("Enter the size of array B: "))
arr2 = list(map(int, input("Enter the space-separated values of array B: ").strip().split()))

def odd_ele(arr1,arr2):
    common_ele_odd=[]
    for i in arr1:
        if i%2!=0 and i in arr2:
            common_ele_odd.append(i)
    print(" ".join(map(str, sorted(common_ele_odd))) if common_ele_odd else "No common odd elements found.")
      
odd_ele(arr1,arr2)       

