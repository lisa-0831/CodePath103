"""
Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

############### UMPIRE Method ###############

1. Understand
Input: list of strings operations
Output: final integer value of tigger

Start tigger at 1.
"bouncy" or "flouncy" -> +1
"trouncy" or "pouncy" -> -1
Edge case: empty list -> 1

2. Match
This is a list traversal problem.
Use a counter variable and update it for each operation.

3. Plan
Initialize tigger = 1.
Loop through operations.
If operation is "bouncy" or "flouncy", increment tigger.
If operation is "trouncy" or "pouncy", decrement tigger.
Return tigger.

4. Implement
Use a for loop and if/else conditionals.

5. Review
Example: ["trouncy", "flouncy", "flouncy"]
Start tigger = 1
"trouncy" -> 0
"flouncy" -> 1
"flouncy" -> 2
Return 2

6. Evaluate
Time complexity: O(n), where n is the number of operations.
Space complexity: O(1), because only one counter is used.

"""

def final_value_after_operations(operations):
    counter = 1
    for operation in operations:
      if operation == "bouncy" or operation == "flouncy":
        counter += 1
      elif operation == "trouncy" or operation == "pouncy":
        counter -= 1
    return counter

# Example Usage:
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# Example Output:
# 2
# 4