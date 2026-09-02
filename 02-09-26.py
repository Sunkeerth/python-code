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
n=int(input("enter the n value number : "))
arr=list(map(int,input("ener the array values :  ").strip().split()))


# def missing_val(arr):
#     n=len(arr)
#     nat=(n+1)*(n+2)//2  # Sum of 1 to (n+1) since one element is missing
#     summ_arr=sum(arr)
#     print("sum of array elements : ",summ_arr)
#     print("natural number sum : ",nat)
#     return nat - summ_arr

# res=missing_val(arr)
# print(res)

"""
📝 Problem StatementTitle: Largest Repeating ElementDifficulty: MediumDescription:Given a sorted array of integers in
ascending order, find the element that repeats most frequently. If there is a tie where multiple elements share the 

highest frequency, return the element that appears latest in the array (the largest value due to the sorted nature)

.Input Format:The first line contains an integer n, representing the size of the array.The second line contains n 

space-separated integers representing the elements of the sorted array.Output Format:Print the largest repeating 
element based on maximum frequency."""

def largest_repeating_element(arr):
    arr.sort()
    max_count=1
    for i in range(len(arr)):
        count =1
        if i>0 and arr[i]==arr[i-1]:
            count+=1
        if count>max_count:
            max_count=count
            result=arr[i]   
    

result=largest_repeating_element(arr)
print("Largest repeating element is : ",result)