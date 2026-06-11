"""
Problem 3: Find All Duplicate Treasure Chests in an Array
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

############### UMPIRE Method ###############

1. Understand
Input: a list of integers chests
Output: a list of integers that appear twice
Each number appears once or twice.
Edge case: empty list or no duplicates -> empty list

2. Match
This is a set problem.
Use a set to track which chest numbers have already been seen.

3. Plan
Create an empty set called seen.
Create an empty list called duplicates.
Loop through each chest in chests.
If chest is already in seen, add it to duplicates.
Otherwise, add chest to seen.
Return duplicates.

4. Implement
Use a for loop and set membership checks.

5. Review
For [4, 3, 2, 7, 8, 2, 3, 1]:
2 and 3 appear twice, so return [2, 3].
For [1, 1, 2], return [1].
For [1], return [].

6. Evaluate
Time complexity: O(n), where n is the length of chests.
Space complexity: O(n), because we use a set to store seen values.

"""

def find_duplicate_chests(chests):
    seen = set()
    duplicates = []

    for chest in chests:
        if chest in seen:
            duplicates.append(chest)
        else:
            seen.add(chest)

    return duplicates

# Example Usage:
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

# Example Output:
# [2, 3]
# [1]
# []