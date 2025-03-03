# Creating a Set
fruits = {"apple", "banana", "cherry"}
print("Fruits Set:", fruits)

# Creating an Empty Set (IMPORTANT)
empty_set = set()  # ✅ Correct way
not_a_set = {}     # ❌ Creates an empty dictionary

# Creating a Set from a List (Removes Duplicates)
numbers = set([1, 2, 3, 4, 4, 5])
print("Unique Numbers:", numbers)
