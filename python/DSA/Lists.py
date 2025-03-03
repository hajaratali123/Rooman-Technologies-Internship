# 1️⃣ Lists in Python (Dynamic Arrays)
# A list is an ordered, mutable (changeable) collection 
# of elements. It can contain different data types like integers, 
# strings, and even other lists.

# ✅ Creating a List

# A list can store multiple data types
my_list = [10, "Hello", 3.14, True]
print(my_list)  # Output: [10, "Hello", 3.14, True]


# ✅ Accessing Elements

print(my_list[0])   # Output: 10 (First element)
print(my_list[-1])  # Output: True (Last element)


# ✅ Modifying a List

my_list[1] = "World"  # Changing an element
print(my_list)  # Output: [10, "World", 3.14, True]

# ✅ Adding Elements
my_list.append(100)   # Adds 100 at the end
print(my_list)  # Output: [10, "World", 3.14, True, 100]

my_list.insert(2, "Python")  # Inserts "Python" at index 2
print(my_list)  # Output: [10, "World", "Python", 3.14, True, 100]

# ✅ Removing Elements

my_list.remove("World")  # Removes "World"
print(my_list)  # Output: [10, "Python", 3.14, True, 100]

my_list.pop()  # Removes the last element
print(my_list)  # Output: [10, "Python", 3.14, True]

# ✅ Looping Through a List

for item in my_list:
    print(item)