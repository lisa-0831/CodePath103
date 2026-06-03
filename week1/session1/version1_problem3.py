"""
Problem 3: T-I-Double Guh-Er II
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

############### UMPIRE Method ###############

1. Understand
Input: string word
Output: a new lowercase string with "t", "i", "gg", and "er" removed
The function is case insensitive, so uppercase letters should be treated as lowercase.
Edge case: empty string -> empty string

2. Match
This is a string manipulation problem.
Use traversal and build a new result string.

3. Plan
Convert word to lowercase.
Loop through the string using an index.
If the current substring is "gg" or "er", skip 2 characters.
If the current character is "t" or "i", skip 1 character.
Otherwise, add the character to the result.
Return the result.

4. Implement
Use a while loop so we can skip either 1 or 2 characters.

5. Review
For "Trigger":
lowercase -> "trigger"
remove "t", "i", "gg", "er" -> "r"

For "eggplant" -> "eplan"
For "Choir" -> "chor"

6. Evaluate
Time complexity: O(n), where n is the length of word.
Space complexity: O(n), because we build a new string.

"""

def tiggerfy(word):
	word = word.lower()
	result = ""
	i = 0
	while i < len(word):
		if word[i:i + 2] == "gg" or word[i:i + 2] == "er":
			i += 2
		elif word[i] == "t" or word[i] == "i":
			i += 1
		else:
			result += word[i]
			i += 1
	return result

# Example Usage:
word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word)) 

# Example Output:
# "r"
# "eplan"
# "chor"