"""
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

############### UMPIRE Method ###############

1. Understand
Input: a list lst
Output: the same list with elements in reverse order
The list should be reversed in-place.
Do not use list slicing.
Edge cases: empty list or one element -> list stays the same

2. Match
This is a two-pointer list problem.
Use one pointer at the start and one pointer at the end.

3. Plan
Set left to the first index and right to the last index.
While left is less than right, swap lst[left] and lst[right].
Move left forward and right backward.
Return lst.

4. Implement
Use a while loop and swap the values at the two pointers.

5. Review
For ["pooh", "christopher robin", "piglet", "roo", "eeyore"]:
Swap "pooh" and "eeyore".
Swap "christopher robin" and "roo".
"piglet" stays in the middle.
Return ["eeyore", "roo", "piglet", "christopher robin", "pooh"].

6. Evaluate
Time complexity: O(n), where n is the length of lst.
Space complexity: O(1), because the list is reversed in-place.

"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst

# Example Usage
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

# Example Output:
# ["eeyore", "roo", "piglet", "christopher robin", "pooh"]
