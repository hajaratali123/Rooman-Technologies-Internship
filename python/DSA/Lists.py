# List Operations and Functions in Python

# 1️⃣ Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

try:
    result=0
    for num in my_list:
        result = result+num
    print(f"the result is {result}")
except IndexError:
    print("error",KeyError)


# try:
#     my_list=[1,2,3,4,5,6]
#     print(my_list[4])
# except IndexError:
#     print("index of range")

len = len(my_list)
index = 3

if index < 0 or index >= len:
    print("Index out of range")
else:
    print(my_list[index])

# 2️⃣ Accessing elements
print("First element:", my_list[0])   # Accessing by index
print("Last element:", my_list[-1])   # Negative indexing

# 3️⃣ Adding elements
my_list.append(60)  # Adds an element at the end
my_list.insert(2, 25)  # Inserts 25 at index 2
new_elements = [70, 80]
my_list.extend(new_elements)  # Extends list with multiple elements
print("List after adding elements:", my_list)

# 4️⃣ Adding element at a user-defined position
position = int(input("Enter the position to add an element: "))  # Get index from user
element = int(input("Enter the element to add: "))  # Get element from user
if 0 <= position <= len(my_list):
    my_list.insert(position, element)  # Insert at given position
    print(f"List after adding {element} at position {position}:", my_list)
else:
    print("Invalid position!")

# 5️⃣ Removing elements
my_list.remove(30)  # Removes first occurrence of 30
print("After removing 30:", my_list)

my_list.pop()  # Removes last element
print("After popping last element:", my_list)

my_list.pop(2)  # Removes element at index 2
print("After popping index 2:", my_list)

del my_list[1]  # Deletes element at index 1
print("After deleting index 1:", my_list)

# 6️⃣ Checking repetition of an element
check_value = int(input("Enter an element to check its occurrence: "))  # User input
count = my_list.count(check_value)  # Count occurrences
if count > 0:
    print(f"The element {check_value} appears {count} times in the list.")
else:
    print(f"The element {check_value} is not in the list.")

# 7️⃣ Searching in a list
search_value = 40
if search_value in my_list:
    print(f"{search_value} found at index:", my_list.index(search_value))
else:
    print(f"{search_value} not found in list")

# 8️⃣ Sorting and reversing
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Ascending order
print("Sorted list:", numbers)

numbers.sort(reverse=True)  # Descending order
print("Descending sorted list:", numbers)

numbers.reverse()  # Reverse order
print("Reversed list:", numbers)

# 9️⃣ Copying a list
list_copy = my_list.copy()
print("Copied list:", list_copy)

# 🔟 List comprehension (Advanced)
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared numbers:", squared_numbers)

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

# 1️⃣1️⃣ Clearing the list
my_list.clear()
print("List after clearing:", my_list)

# 1️⃣2️⃣ Concatenating lists (Merging lists together)
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Method 1: Using the + operator
concatenated_list = list1 + list2
print("Concatenated List using +:", concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Method 2: Using extend() method
list1.extend(list2)
print("Concatenated List using extend():", list1)  # Output: [1, 2, 3, 4, 5, 6]

# Method 3: Using list comprehension
list3 = [x for x in list1] + [x for x in list2]
print("Concatenated List using list comprehension:", list3)

# 1️⃣3️⃣ Slicing a list
sliced_list = my_list[1:4]  # Slices from index 1 to 3 (not including 4)
print("Sliced list:", sliced_list)

# 1️⃣4️⃣ List Comprehension
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# 1️⃣5️⃣ List Functions
my_list = [1, 2, 3, 4, 5]
sum_result = sum(my_list)  # Sums all elements
print("Sum of elements:", sum_result)

max_result = max(my_list)  # Finds the maximum element  
