"""
Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

############### UMPIRE Method ###############

1. Understand
Input: a string message with lowercase English letters and whitespace
Output: True if message contains every letter of the alphabet at least once, otherwise False
Edge case: empty string -> False

2. Match
This is a set problem.
Use a set to quickly check which letters appear in the message.

3. Plan
Create a set from message.
Loop through each letter in the alphabet.
If any alphabet letter is missing from the set, return False.
If all letters are found, return True.

4. Implement
Use set(message) to store unique characters.
Use a for loop over "abcdefghijklmnopqrstuvwxyz".

5. Review
For "sphinx of black quartz judge my vow", every letter appears, so return True.
For "trust me", many letters are missing, so return False.

6. Evaluate
Time complexity: O(n), where n is the length of message.
Space complexity: O(n), because the set stores unique characters from message.

"""

def can_trust_message(message):
    letters = set(message)
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in letters:
            return False
    return True

# Example Usage:
message1 = "sphinx of black quartz judge my vow"
print(can_trust_message(message1))

message2 = "trust me"
print(can_trust_message(message2))

# Example Output:
# True
# False