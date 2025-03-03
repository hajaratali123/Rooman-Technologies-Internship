# 2️⃣ Tuples in Python (Immutable Ordered Collection)
# A tuple is like a list but immutable (cannot be changed after creation). It is used for fixed data.
# Tuple Operations and Functions in Python

# 1️⃣ Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# 2️⃣ Accessing Elements
print("First Element:", my_tuple[0])   # Indexing
print("Last Element:", my_tuple[-1])   # Negative Indexing

# 3️⃣ Slicing a Tuple
print("Elements from index 1 to 3:", my_tuple[1:4])  # Slicing

# 4️⃣ Checking if an Element Exists
search_value = 30
if search_value in my_tuple:
    print(f"{search_value} exists in the tuple.")
else:
    print(f"{search_value} not found in the tuple.")

# 5️⃣ Finding Index of an Element
if search_value in my_tuple:
    print(f"Index of {search_value}:", my_tuple.index(search_value))

# 6️⃣ Counting Occurrences of an Element
repeated_tuple = (1, 2, 2, 3, 4, 4, 4, 5)
check_value = 4
print(f"The element {check_value} appears {repeated_tuple.count(check_value)} times in the tuple.")

# 7️⃣ Concatenating Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2  # Using `+` operator
print("Concatenated Tuple:", concatenated_tuple)

# 8️⃣ Repeating a Tuple (Multiplication)
repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)

# 9️⃣ Iterating Over a Tuple
print("Iterating Over Tuple:")
for item in my_tuple:
    print(item, end=" ")

print()  # Newline

# 🔟 Tuple Length
print("Length of Tuple:", len(my_tuple))

# 1️⃣1️⃣ Converting a List to a Tuple
my_list = [100, 200, 300]
converted_tuple = tuple(my_list)
print("Converted Tuple from List:", converted_tuple)

# 1️⃣2️⃣ Converting a Tuple to a List (For Modification)
modifiable_list = list(my_tuple)
modifiable_list.append(60)  # Adding an element after conversion
print("Modified List after Adding an Element:", modifiable_list)

# 1️⃣3️⃣ Unpacking a Tuple
a, b, c, d, e = my_tuple  # Unpacking tuple into variables
print("Unpacked Values:", a, b, c, d, e)

# 1️⃣4️⃣ Nested Tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing Nested Tuple Element:", nested_tuple[1][1])  # Accessing value inside nested tuple

# 1️⃣5️⃣ Tuple with a Single Element (Must have a comma)
single_element_tuple = (10,)  # Without a comma, it's just an integer
print("Single Element Tuple:", single_element_tuple)

# 1️⃣6️⃣ Clearing a Tuple (Tuples are immutable, so we reassign an empty tuple)
my_tuple = ()
print("Tuple after Clearing:", my_tuple)
