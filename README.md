# Bubble-sort

Bubble sort is an algorithm that compares the adjacent elements and swaps their positions if they are not in the intended order. The order can be ascending or descending.

# Approach of Bubble sort
## Starting from the first index, compare the first and the second elements.If the first element is greater than the second element, they are swapped.Now, compare the second and the third elements. Swap them if they are not in order.The above process goes on until the last element.

## The same process goes on for the remaining iterations. After each iteration, the largest element among the unsorted elements is placed at the end.In each iteration, the comparison takes place up to the last unsorted element.The array is sorted when all the unsorted elements are placed at their correct positions.




# Complexity: O(n2)

Also, we can analyze the complexity by simply observing the number of loops. There are 2 loops so the complexity is n*n = n2
# Time Complexities:

## Worst Case Complexity:O(n2)
If we want to sort in ascending order and the array is in descending order then, the worst case occurs.

## Best Case Complexity:O(n)
If the array is already sorted, then there is no need for sorting.

## Average Case Complexity:O(n2)
It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

# Space Complexity:
Space complexity is O(1) because an extra variable temp is used for swapping.

In the optimized algorithm, the variable swapped adds to the space complexity thus, making it O(2).


# Bubble Sort Applications
Bubble sort is used in the following cases where

1. the complexity of the code does not matter.
2. a short code is preferred.
