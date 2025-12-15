a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # List of integers
# result = a[1:5]
a.append(11)
print("List:", a)
# print("Sliced List (index 1 to 4):", result)

tuples = (1, 2, 3, 4, 5) # Tuple of integers
print("Tuple:", tuples)
# tuples.[3] = 10 tuples does not support item assignment

set  = {1, 2, 3, 4, 5, 5} # Set of integers
set.add(6)
print("Set:", set)

dictionary = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Dictionary:", dictionary["name"])
print("Dictionary:", dictionary["age"])
print("Dictionary:", dictionary["city"])
