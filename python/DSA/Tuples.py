# 2️⃣ Tuples in Python (Immutable Ordered Collection)
# A tuple is like a list but immutable (cannot be changed after creation). It is used for fixed data.

# ✅ Creating a Tuple

my_tuple = (10, "Hello", 3.14, True)
print(my_tuple)  # Output: (10, "Hello", 3.14, True)

# ✅ Accessing Elements

print(my_tuple[0])   # Output: 10
print(my_tuple[-1])  # Output: True

# ✅ Immutable Property
# Tuples cannot be modified after creation.


my_tuple[1] = "World"  # ❌ This will give an error

# ✅ Looping Through a Tuple

for item in my_tuple:
    print(item)

# ✅ Tuple Packing & Unpacking

person = ("Ali", 22, "Developer")  # Packing
name, age, job = person  # Unpacking
print(name, age, job)  # Output: Ali 22 Developer