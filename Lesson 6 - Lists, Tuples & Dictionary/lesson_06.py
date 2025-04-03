# Lesson 06: Lists, Tuples & Dictionary

# Example 1: Working with Lists
# Create a list of names aur addresses
addresses = [
    {"name": "Kako", "address": "Lahore, Pakistan"},
    {"name": "Hussien", "address": "Karachi, Pakistan"},
]

# Printing all names aur addresses
for person in addresses:
    print(f"Name: {person['name']}, Address: {person['address']}")

# Example 2: Accessing List Elements
# Access aur print karo pehla address from the list
print("\nPehla address from the list:")
print(addresses[0])

# Example 3: Modifying Lists
# Add karna hai new entry
addresses.append({"name": "Ali", "address": "Islamabad, Pakistan"})
print("\nUpdated list after adding a new person:")
print(addresses)

# Example 4: List Slicing
# Slice aur print karo pehle 2 logon ka data
print("\nPehle do log list mein:")
print(addresses[:2])

# Example 5: Common List Methods
# Last entry ko remove karna hai using pop()
addresses.pop()
print("\nList after removing the last entry using pop:")
print(addresses)

# Example 6: Sorting a List (By Name)
addresses.sort(key=lambda x: x['name'])
print("\nList sorted by name:")
print(addresses)

# Example 7: Iterating Over Lists with List Comprehension
names = [person['name'] for person in addresses]
print("\nNames from the addresses list using list comprehension:")
print(names)

# Example 8: Tuples in Python
# Create ek tuple
person_tuple = ("Kako", "Lahore", 25)
print("\nTuple with name, city, aur age:")
print(person_tuple)

# Example 9: Dictionaries in Python
# Create ek dictionary with personal information
person_info = {"name": "Hussien", "age": 30, "city": "Karachi"}

# Access karna ek dictionary value
print("\nAccess kar rahe hain value from dictionary:")
print(person_info["city"])

# Modifying ek dictionary value
person_info["age"] = 31
print("\nModified dictionary after changing age:")
print(person_info)

# Example 10: Deleting Items from a Dictionary
del person_info["city"]
print("\nDictionary after deleting city:")
print(person_info)

# Example 11: Iterating Over a Dictionary
for key, value in person_info.items():
    print(f"{key}: {value}")

# Conclusion
#Is lesson mein hum ne lists, tuples, aur dictionaries ko explore kiya. Hum ne dekha kaise unhe create, modify, aur iterate kiya jata hai, aur kaise lists ko slice, sort, aur dictionaries ko modify kiya jata hai.
