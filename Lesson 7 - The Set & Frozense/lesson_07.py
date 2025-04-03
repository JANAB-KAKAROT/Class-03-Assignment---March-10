# Lesson 07: The Set & Frozenset
# Introduction to Set and Frozenset in Python
# Sets are collections of unique elements. They are unordered, and you cannot have duplicate values in them.

# Example 1: Creating a Set
# Sets mein sirf unique elements hote hain, duplicates nahi hote

# Set creation example
kako_set = {"Kako", "Hussien", "Ali", "Ayesha", "John", "Khan", "Hussien"}
print("Original Set (Kako Set):", kako_set)

# Adding an element to the set
kako_set.add("Zain")
print("\nSet after adding Zain:", kako_set)

# Removing an element from the set
kako_set.remove("Ali")
print("\nSet after removing 'Ali':", kako_set)

# Checking if an element is in the set
if "John" in kako_set:
    print("\nJohn is in the set.")
else:
    print("\nJohn is not in the set.")

# Set Operations
# Union of two sets
another_set = {"Ayesha", "Zain", "Ahmed"}
union_set = kako_set.union(another_set)
print("\nUnion of sets:", union_set)

# Intersection of two sets
intersection_set = kako_set.intersection(another_set)
print("\nIntersection of sets:", intersection_set)

# Difference of two sets
difference_set = kako_set.difference(another_set)
print("\nDifference of sets (Kako Set - Another Set):", difference_set)

# Set with different data types
mixed_set = {1, 3.14, "Kako", (1, 2, 3)}
print("\nSet with mixed data types:", mixed_set)

# Example 2: Creating a Frozenset
# Frozenset ki khasiyat ye hai ke ye immutable hota hai, yaani iske elements ko modify nahi kiya ja sakta

# Frozenset creation example
kako_frozenset = frozenset(kako_set)
print("\nFrozen Set (Kako Frozenset):", kako_frozenset)

# Trying to add an element to a Frozenset (will raise an error)
try:
    kako_frozenset.add("New Element")
except AttributeError as e:
    print("\nError (Cannot add to frozen set):", e)

# Set and Frozenset Comparison
print("\nIs frozen set equal to the original set?", kako_frozenset == kako_set)

# Practical Example 1: Student Registration System (Using Set)
students = {"Kako", "Hussien", "Ali", "Sara", "Ayesha"}
print("\nRegistered Students:", students)

# Adding a new student
students.add("Zain")
print("\nAfter adding Zain:", students)

# Trying to add a duplicate student (it will not be added)
students.add("Ayesha")
print("\nAfter trying to add duplicate 'Ayesha':", students)

# Practical Example 2: Unique Items in a Store Inventory (Using Frozenset)
inventory_items = frozenset(["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"])
print("\nStore Inventory (Frozenset):", inventory_items)

# Inventory cannot be modified as it's a Frozenset
# Trying to add or remove items will result in an error:
try:
    inventory_items.add("Mouse")
except AttributeError as e:
    print("\nError (Cannot modify Frozenset):", e)

# Operations on Sets
# Example: Comparing two sets of students for common ones
students_in_karachi = {"Kako", "Hussien", "Ali", "Sara", "Ahmed"}
students_in_lahore = {"John", "Sara", "Ayesha", "Ali", "Zain"}

common_students = students_in_karachi.intersection(students_in_lahore)
print("\nCommon Students in Karachi and Lahore:", common_students)

# Using Set to Remove Duplicates from List
student_list = ["Kako", "Sara", "Hussien", "Ali", "Ayesha", "Hussien", "John"]
unique_students = set(student_list)
print("\nUnique Students from List:", unique_students)

# Example: Working with Frozenset for Immutable Data
frozen_inventory = frozenset(["Laptop", "Mobile", "Tablet"])
print("\nFrozen Inventory (Immutable):", frozen_inventory)

# Operations on frozen sets: You can perform operations like union, intersection, etc., but cannot modify the elements.
new_inventory = frozenset(["Mouse", "Keyboard"])
updated_inventory = frozen_inventory.union(new_inventory)
print("\nUpdated Frozenset (after Union with new items):", updated_inventory)

