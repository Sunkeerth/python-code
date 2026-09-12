"""
PROBLEM STATEMENT: Pairs with Product
Find pairs of numbers from the array whose product is equal to a given target value.

INPUT FORMAT:
- The first line contains an integer N, representing the size of the array.
- The second line contains N space-separated integers, representing the elements of the array.
- The third line contains a single integer k, representing the desired product value.

OUTPUT FORMAT:
- Print each pair of numbers on a new line, separated by a space.

CONSTRAINTS:
- 1 <= N <= 1000
- -1000 <= Array elements <= 1000
- -10^9 <= k <= 10^9

SAMPLE CASE 1:
Input:
6
2 4 6 3 8 9
12
Output:
2 6
4 3

SAMPLE CASE 2:
Input:
4
2 1 4 3
12
Output:
4 3
"""

n= int(input("enter the n value size of array :    "))
arr=list(map(int, input("enter the space-separated values of array :").strip().split()))
k=int(input("enter the target product value :    "))

def find_pair_of_prod(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j]==k:
                print(arr[i],arr[j])
find_pair_of_prod(arr,k)

