"""
Problem 3: Gallery Wall
You are tasked with organizing a collection of art prints represented by a list of strings collection. You need to display these prints on a single wall in a 2D array format that meets the following criteria:

The 2D array should contain only the elements of the array collection.
Each row in the 2D array should contain distinct strings.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them. Note that the 2D array can have a different number of elements on each row.

############### UMPIRE Method ###############

1. Understand
Input: a list of strings collection
Output: a 2D list that uses every print from collection
Each row must contain distinct strings.
The number of rows should be minimal.
Edge case: empty collection -> empty list

2. Match
This is a frequency map problem.
The minimum number of rows is the highest frequency of any print.

3. Plan
Count how many times each print appears.
Create one row for each needed copy of the most frequent print.
For each print, place each copy in a different row.
Return the rows.

4. Implement
Use a dictionary to count prints.
Use nested loops to add each print to separate rows.

5. Review
For ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]:
"O'Keefe" appears 3 times, so we need 3 rows.
Place each duplicate in a different row.
Return a valid 2D list with 3 rows.

6. Evaluate
Time complexity: O(n), where n is the length of collection.
Space complexity: O(n), because we store counts and the output list.

"""

def organize_exhibition(collection):
    counts = {}

    for print_name in collection:
        if print_name in counts:
            counts[print_name] += 1
        else:
            counts[print_name] = 1

    rows = []

    for print_name in counts:
        while len(rows) < counts[print_name]:
            rows.append([])

        for row in range(counts[print_name]):
            rows[row].append(print_name)

    return rows

# Example Usage:

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))

# Example Output:

# [
#   ["O'Keefe", "Kahlo", "Picasso", "Warhol"],
#   ["O'Keefe", "Kahlo"],
#   ["O'Keefe"]
# ]
# Example 1 Explanation:
# All elements of collections were used, and each row of the 2D array contains 
# distinct strings, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.

# [["Kusama", "Monet", "Ofili", "Banksy"]]
# Example 2 Explanation: 
# All elements of the array are distinct, so we can keep all of them in the first 
# row of the 2D array.