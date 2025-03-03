# 1️⃣ Creating a Dictionary
person = {
    "name": "Ali",
    "age": 22,
    "city": "Bangalore",
    "profession": "Engineer"
}

print("Person Details:", person)

# 2️⃣ Accessing Elements Safely
print("City:", person.get("city", "Not Found"))

# 3️⃣ Adding New Key-Value Pair
person["phone"] = "9876543210"
print("Updated Dictionary:", person)

# 4️⃣ Removing a Key
person.pop("age")
print("After Removing Age:", person)

# 5️⃣ Iterating Over Dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# 6️⃣ Counting Words in a Sentence
sentence = "hello world hello python world"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word Frequency:", word_count)

# 7️⃣ Finding the Student with the Highest Marks
students = {
    "Ali": 85,
    "Sarah": 92,
    "David": 78
}
top_student = max(students, key=students.get)
print("Top Student:", top_student, "Marks:", students[top_student])

# 8️⃣ Merging Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}  # Overwrites 'b'
print("Merged Dictionary:", merged_dict)
