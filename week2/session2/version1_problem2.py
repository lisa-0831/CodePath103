"""
Problem 2: Verifying Authenticity
Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].

The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

############### UMPIRE Method ###############

1. Understand
Input: a list of integers art_pieces
Output: True if art_pieces is a permutation of base[n], otherwise False
base[n] contains 1 through n once, except n appears twice.
The length of base[n] is n + 1.
Edge case: empty list -> False

2. Match
This is a frequency map problem.
We need to count how many times each number appears.

3. Plan
If art_pieces is empty, return False.
Find n by getting the maximum value in art_pieces.
Check that the length of art_pieces is n + 1.
Count each value in art_pieces.
For numbers 1 through n - 1, each count should be 1.
The count of n should be 2.
Return True if all checks pass.

4. Implement
Use a dictionary to count each number.
Use a for loop to check the expected numbers.

5. Review
For [1, 3, 3, 2], n = 3 and the counts match base[3], so return True.
For [2, 1, 3], n = 3 but the length is not 4, so return False.
For [1, 1], n = 1 and count of 1 is 2, so return True.

6. Evaluate
Time complexity: O(n), where n is the maximum value in art_pieces.
Space complexity: O(n), because the dictionary stores counts.

"""

def is_authentic_collection(art_pieces):
  if not art_pieces:
    return False

  n = max(art_pieces)
  if len(art_pieces) != n + 1:
    return False

  counts = {}
  for piece in art_pieces:
    counts[piece] = counts.get(piece, 0) + 1

  for piece in range(1, n):
    if counts.get(piece, 0) != 1:
      return False

  return counts.get(n, 0) == 2

# Example Usage:

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]
collection4 = [2, 2, 3]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
print(is_authentic_collection(collection4))

# Example Output:

# False
# Example 1 Explanation: Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# However, base[3] has four elements but array collection1 has three. Therefore, 
# it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# True
# Example 2 Explanation:  Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# It can be seen that collection2 is a permutation of base[3] = [1, 2, 3, 3] 
# (by swapping the second and fourth elements in nums, we reach base[3]).
#  Therefore, the answer is true.

# True
# Example 3 Explanation; Since the maximum element of the array is 1, 
# the only candidate n for which this array could be a permutation of base[n], 
# is n = 1. It can be seen that collection3 is a permutation of base[1] = [1, 1].
#  Therefore, the answer is true.

 # False