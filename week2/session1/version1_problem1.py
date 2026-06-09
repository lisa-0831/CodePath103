"""
Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

############### UMPIRE Method ###############

1. Understand
Input: a dictionary treasure_map
Keys are location names and values are treasure counts.
Output: the total number of treasures.
Edge case: empty dictionary -> 0

2. Match
This is a dictionary traversal problem.
We need to add all the values together.

3. Plan
Create a total variable and set it to 0.
Loop through each location in treasure_map.
Add the treasure count at that location to total.
Return total.

4. Implement
Use a for loop to iterate through the dictionary keys.
Use treasure_map[location] to access each value.

5. Review
For {"Cove": 3, "Beach": 7, "Forest": 5}:
Start total = 0.
Add 3, then 7, then 5.
Return 15.

6. Evaluate
Time complexity: O(n), where n is the number of locations.
Space complexity: O(1), because only one total variable is used.

"""

def total_treasure(treasure_map):
    total = 0

    for location in treasure_map:
        total += treasure_map[location]

    return total

# Example Usage:
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}
print(total_treasure(treasure_map1)) 

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}
print(total_treasure(treasure_map2))

# Example Output:
# 15
# 50