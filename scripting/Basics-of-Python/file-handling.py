# f = open("data.txt", "r") read a file

f = open("data.txt", "r+")

data = f.readline()

print(data)

f.write("Hello, World!")

f.close()