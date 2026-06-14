"""
Problem 1: Arrange Guest Arrival Order
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on a set of instructions.

The instructions are provided as a 0-indexed string arrival_pattern of length n, consisting of the characters:

'I' - The next guest should have a higher number than the previous guest.
'D' - The next guest should have a lower number than the previous guest.
You need to create a string guest_order of length n + 1 that satisfies the following conditions:

guest_order contains each number from 1 to str(n + 1) exactly once. These numbers represent the guests' assigned numbers.
For every index i from 0 to n - 1:
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Among all valid orders, return the lexicographically smallest one.

############### UMPIRE Method ###############

1. Understand
Input: a string arrival_pattern containing "I" and "D"
Output: the lexicographically smallest guest_order string that follows the pattern
Use each number from 1 to n + 1 exactly once.
"I" means the next number should be bigger.
"D" means the next number should be smaller.
Edge case: empty pattern -> "1"

2. Match
This is a stack problem.
A stack helps reverse groups of numbers when we see consecutive "D" characters.

3. Plan
Create an empty stack and output list.
Loop from 1 to n + 1.
Push each number onto the stack.
When we reach an "I" or the end of the pattern, pop everything from the stack into output.
Join output into a string and return it.

4. Implement
Use a for loop from 0 to n.
Use stack.append() to add numbers.
Use stack.pop() to add numbers to output in reverse order when needed.

5. Review
For "DDD":
Push 1, 2, 3, 4.
At the end, pop all values -> 4, 3, 2, 1.
Return "4321".

For "IIIDIDDD":
The stack pops after each "I" and after the final group of "D"s.
Return "123549876".

6. Evaluate
Time complexity: O(n), where n is the length of arrival_pattern.
Space complexity: O(n), because the stack and output list store the numbers.

"""

def arrange_guest_arrival_order(arrival_pattern):
  stack = []
  output = []

  n = len(arrival_pattern)

  for i in range(n + 1):
      stack.append(i + 1)

      if i == n or arrival_pattern[i] == 'I':
          while stack:
              output.append(stack.pop())

  return ''.join(map(str, output))

# Example Usage: 
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

# Example Output:
# 123549876
# 4321