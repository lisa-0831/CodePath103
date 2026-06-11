"""
Problem 1: Balanced Art Collection
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of art pieces are balanced to attract the right range of buyers. A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

############### UMPIRE Method ###############

1. Understand
Input: a list of integers art_pieces
Output: the length of the longest balanced subsequence
A balanced subsequence has max value - min value exactly 1.
Edge case: empty list or all same values -> 0

2. Match
This is a frequency map problem.
We need to count values and compare numbers that differ by 1.

3. Plan
Create a dictionary to count how many times each value appears.
Loop through each value in art_pieces and update its count.
Loop through each value in the dictionary.
If value + 1 exists, combine their counts.
Track the largest combined count.
Return the largest count.

4. Implement
Use a dictionary for counts.
Use a variable longest to store the best answer.

5. Review
For [1, 3, 2, 2, 5, 2, 3, 7]:
2 appears 3 times and 3 appears 2 times.
Together they make a balanced subsequence of length 5.
Return 5.
For [1, 1, 1, 1], no pair differs by 1, so return 0.

6. Evaluate
Time complexity: O(n), where n is the number of art pieces.
Space complexity: O(n), because the dictionary stores the counts.

"""

def find_balanced_subsequence(art_pieces):
    counts = {}
    for piece in art_pieces:
        if piece in counts:
            counts[piece] += 1
        else:
            counts[piece] = 1

    longest = 0
    for piece in counts:
        if piece + 1 in counts:
            longest = max(longest, counts[piece] + counts[piece + 1])

    return longest

# Example Usage:
art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

# Example Output:
# 5 (Example 1 Explanation: The longest balanced subsequence is [3,2,2,2,3].)
# 2
# 0