"""
Problem 4: Non-decreasing Array
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

############### UMPIRE Method ###############

1. Understand
Input: a list of integers nums
Output: True if nums can become non-decreasing by changing at most one element, otherwise False
Non-decreasing means every nums[i] <= nums[i + 1].
Edge cases: empty list, one element, or already non-decreasing list -> True

2. Match
This is an array traversal problem.
We need to count how many times the order decreases.

3. Plan
Loop through nums and look for places where nums[i] > nums[i + 1].
Keep a count of how many decreases we find.
If there is more than one decrease, return False.
When there is one decrease, decide whether to change nums[i] or nums[i + 1].
Return True if the loop finishes with at most one change.

4. Implement
Use a for loop and a counter variable.
When nums[i] > nums[i + 1], increment the counter.
Modify one value so the rest of the checks can continue correctly.

5. Review
For [4, 2, 3], change 4 to 2, so return True.
For [4, 2, 1], there are too many decreases, so return False.
For [1, 2, 3], no changes are needed, so return True.

6. Evaluate
Time complexity: O(n), where n is the length of nums.
Space complexity: O(1), because only a counter is used.

"""

def non_decreasing(nums):
  count = 0

  for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
      count += 1

      if count > 1:
        return False

      if i == 0 or nums[i - 1] <= nums[i + 1]:
        nums[i] = nums[i + 1]
      else:
        nums[i + 1] = nums[i]

  return True

# Example Usage:
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))

# Example Output:
# True
# False