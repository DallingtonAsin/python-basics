# File Input/Output

with open("words.txt", "w") as file:
    file.write("Hello World!")

with open("words.txt", "r") as file:
    print(file.read())