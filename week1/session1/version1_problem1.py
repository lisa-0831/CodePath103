"""
Problem 1: Hunny Hunt
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.

############### UMPIRE Method ###############

UMPIRE Method

1. Understand
Return the first index where target appears in items. If it never appears, return -1.
Example: ['haycorn', 'hunny'], target = 'hunny' -> 1
Edge case: empty list -> -1

2. Match
This is a linear search problem because we need to check each item in order.

3. Plan
Loop through each index in items. If items[i] equals target, return i. If the loop ends, return -1.

4. Implement
Use a for loop over range(len(items)) and compare each item to target.

5. Review
For ['haycorn', 'haycorn', 'hunny'], target = 'hunny', the loop checks indexes 0, 1, then returns 2.
For ['bed'], target = 'hunny', no match is found, so return -1.

"""

def linear_search(items, target):
	for i in range(len(items)):
		if items[i] == target:
			return i
	return -1

# Example Usage:
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)

# Example Output:
# 3
# -1