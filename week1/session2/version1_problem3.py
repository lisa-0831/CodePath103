"""
Problem 3: Remove Duplicates
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

############### UMPIRE Method ###############

1. Understand
Input: a sorted list items
Output: the length of the list after removing duplicates
Modify items in-place so each element appears only once.
Do not create another list.
Edge case: empty list -> 0

2. Match
This is a two-pointer array problem.
Because the list is sorted, duplicates will be next to each other.

3. Plan
If items is empty, return 0.
Use one pointer to track the position for the next unique item.
Loop through the list with another pointer.
When we find a new unique item, move it to the next unique position.
Return the number of unique items.

4. Implement
Use a write pointer and a read pointer.
Update items in-place when a new value is found.

5. Review
For ["extract of malt", "haycorns", "honey", "thistle", "thistle"]:
The first four values are unique.
The second "thistle" is skipped.
Return 4.

6. Evaluate
Time complexity: O(n), where n is the length of items.
Space complexity: O(1), because no extra list is created.


"""

def remove_dupes(items):
    if not items:
        return 0

    write = 1

    for read in range(1, len(items)):
        if items[read] != items[read - 1]:
            items[write] = items[read]
            write += 1

    return write

# Example Usage
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

# Example Output:
# 4
# 4