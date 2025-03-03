# 1️⃣ Creating a Tuple and Printing Elements
numbers = (10, 20, 30, 40, 50)
print("Tuple Elements:", numbers)
print("First Element:", numbers[0])  # Indexing

# 2️⃣ Taking User Input for a Tuple
user_values = tuple(map(int, input("Enter numbers separated by space: ").split()))
print("User Tuple:", user_values)
print("Length of Tuple:", len(user_values))

# 3️⃣ Slicing a Tuple
print("Sliced Tuple (index 2 to 5):", numbers[2:5])

# 4️⃣ Checking Membership in Tuple
words = ("apple", "banana", "cherry", "date")
word_check = input("Enter a word to check: ")
print(f"'{word_check}' exists in tuple:", word_check in words)

# 5️⃣ Finding the Index of an Element
find_value = int(input("Enter a number to find its index: "))
if find_value in numbers:
    print(f"Index of {find_value}:", numbers.index(find_value))
else:
    print("Value not found in tuple.")

# 6️⃣ Counting Occurrences of an Element
count_value = int(input("Enter a number to count: "))
print(f"{count_value} appears {numbers.count(count_value)} times.")

# 7️⃣ Concatenating Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Concatenated Tuple:", merged_tuple)

# 8️⃣ Repeating a Tuple
repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)

# 9️⃣ Convert Tuple to List, Modify, and Convert Back
num_list = list(numbers)
num_list.append(60)  # Adding element
modified_tuple = tuple(num_list)
print("Modified Tuple:", modified_tuple)

# 🔟 Sorting a Tuple (Returns a List)
sorted_tuple = tuple(sorted(numbers))
print("Sorted Tuple:", sorted_tuple)

# 1️⃣1️⃣ Comparing Two Tuples
tupleA = (1, 3, 5)
tupleB = (2, 3, 4)
print("Is tupleA < tupleB?", tupleA < tupleB)

# 1️⃣2️⃣ Nested Tuples & Accessing Inner Elements
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing Inner Element:", nested_tuple[1][1])  # Element 3

# 1️⃣3️⃣ Tuple Unpacking
a, b, c, d, e = numbers  # Unpacking values
print("Unpacked Values:", a, b, c, d, e)
