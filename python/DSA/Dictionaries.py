# 3️⃣ Dictionaries in Python (Key-Value Pair)
# A dictionary is an unordered collection of key-value pairs. It is useful for mapping and fast lookups.

# ✅ Creating a Dictionary

student = {
    "name": "Ali",
    "age": 22,
    "course": "Computer Science"
}
print(student)

# ✅ Accessing Values

print(student["name"])  # Output: Ali
print(student.get("age"))  # Output: 22

# ✅ Adding/Updating Elements

student["grade"] = "A"  # Adding a new key-value pair
student["age"] = 23  # Updating an existing key
print(student)

# ✅ Removing Elements

student.pop("grade")  # Removes "grade" key
del student["course"]  # Deletes "course"
print(student)

# ✅ Looping Through a Dictionary

for key, value in student.items():
    print(f"{key}: {value}")


#             🔍 Key Differences
# Feature	    List	    Tuple	    Dictionary
# Order	        Ordered	    Ordered	    Unordered (Python 3.7+ maintains order)
# Mutable?	    Yes	        No	        Yes
# Duplicates?	Yes	        Yes	        No (keys must be unique)
# Indexed?	    Yes	        Yes	        No (uses keys instead)