"""
PROBLEM STATEMENT: Even, Odd and Negative Elements in Array

Write a program to print negative elements, even elements and odd elements 
present in an array separately.

INPUT FORMAT:
- First line contains a single integer N. 
- Next line contains N space-separated integer values.

OUTPUT FORMAT:
- First line prints space-separated negative elements in an array.
- Second line prints space-separated odd elements in an array.
- Third line prints space-separated even elements in an array.

SAMPLE CASE 1:
Input:
6
1 -4 -6 3 10 -20

Output:
-4 -6 -20
1 3
10
"""

n=int(input("enter the n value number : "))
arr=list(map(int,input("ener the array values :  ").strip().split()))
# print(arr)

# def evn_odd_arr_ele(arr):
#     even_ele=[]
#     odd_ele=[]
#     neg_ele=[]
#     for i in arr:
#         if i<0:
#             neg_ele.append(i)
#         elif i%2==0:
#             even_ele.append(i)
#         else:
#             odd_ele.append(i)
#     return neg_ele,odd_ele,even_ele

# result=evn_odd_arr_ele(arr)
# print(" ".join(map(str,result[0]))," :negative elements ")
# print(" ".join(map(str,result[1])), " :odd elements ")
# print(" ".join(map(str,result[2])), " :even elements ")

"""
PROBLEM STATEMENT: Missing Element

Find the missing element in an unsorted array without using sorting.

INPUT FORMAT:
- The first line consists of the size of the array (N).
- Followed by a line containing space-separated integers representing the elements of the array.

OUTPUT FORMAT:
- Output a single integer representing the missing element.

SAMPLE CASE 1:
Input:
6
1 4 2 7 5 3

Output:
6

SAMPLE CASE 2:
Input:
10
1 2 3 6 8 7 4 5 10 11

Output:
9
"""


def missing_val(arr):
    n=len(arr)
    