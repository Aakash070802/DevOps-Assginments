"""def hello_world():
    print("Hello, World! from Python function.")
    return "hey"

hello_world() calling a function
a = hello_world() function return value stored in variable a
print(a) Output the value of a

functions are also known as first-class objects. so we can assign them to variables then that variable can be used to call the function
new = hello_world
a = new()
new()
print(a) calling the function using the new variable"""

def add_numbers(a, b):
    c = a + b
    return c

result = add_numbers(5, 6)

print(result)  # Output: 11