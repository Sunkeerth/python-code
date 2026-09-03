"""
Problem StatementPrint all possible unique pairs of numbers from a given array based on their index positions. For each element at index i, pair it with every
subsequent element at index j (where i < j).Input & Output FormatInput:Line 1: An integer N representing the size of the array.
Line 2: N space-separated integers representing the array elements.Output: Each pair printed on a new line, with elements separated by a space."""

n=int(input("Enter the size of the array: "))
arr=list(map(int,input("Enter the array elements: ").strip().split()))
def print_unique_ele(arr):
    for i in arr:
        for j in arr[arr.index(i)+1:]:
            print(i,j)
print_unique_ele(arr)

"""
# Code Execution Trace Analysis

## Input Configuration
* **Array Size (n):** 5
* **Array Elements (arr):** `[1, 2, 3, 4, 5]`

---

## Line-by-Line Execution Trace

### Step 1: Initialization
* `i` starts at the first element: `1`
* `arr.index(1)` evaluates to `0`
* Inner loop slices `arr[0 + 1:]` which is `arr[1:]` -> `[2, 3, 4, 5]`
* **Inner Loop Iterations (j):**
    * `j = 2` -> Prints: `1 2`
    * `j = 3` -> Prints: `1 3`
    * `j = 4` -> Prints: `1 4`
    * `j = 5` -> Prints: `1 5`

### Step 2: Second Element
* `i` moves to the second element: `2`
* `arr.index(2)` evaluates to `1`
* Inner loop slices `arr[1 + 1:]` which is `arr[2:]` -> `[3, 4, 5]`
* **Inner Loop Iterations (j):**
    * `j = 3` -> Prints: `2 3`
    * `j = 4` -> Prints: `2 4`
    * `j = 5` -> Prints: `2 5`

### Step 3: Third Element
* `i` moves to the third element: `3`
* `arr.index(3)` evaluates to `2`
* Inner loop slices `arr[2 + 1:]` which is `arr[3:]` -> `[4, 5]`
* **Inner Loop Iterations (j):**
    * `j = 4` -> Prints: `3 4`
    * `j = 5` -> Prints: `3 5`

### Step 4: Fourth Element
* `i` moves to the fourth element: `4`
* `arr.index(4)` evaluates to `3`
* Inner loop slices `arr[3 + 1:]` which is `arr[4:]` -> `[5]`
* **Inner Loop Iterations (j):**
    * `j = 5` -> Prints: `4 5`

### Step 5: Fifth Element
* `i` moves to the final element: `5`
* `arr.index(5)` evaluates to `4`
* Inner loop slices `arr[4 + 1:]` which is `arr[5:]` -> `[]` (Empty list)
* **Inner Loop Iterations (j):**
    * No iterations occur because the slice is empty. Nothing is printed.

---

## Final Console Output
```text
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
```

---

## Critical Bug Warning: Duplicate Elements
The current logic relies on `arr.index(i)`. This function **always returns the index of the first occurrence** of a value. If your array contains
duplicate numbers (e.g., `[1, 2, 2, 3]`), the slice will break and cause unexpected duplicate printing or infinite traps for that element's position. """



