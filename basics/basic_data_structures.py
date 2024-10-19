# Lists
from itertools import product

animals = ["dog", "cat", "rabbit", "rabbit"]
for animal in animals:
    print("%s" % animal, end= " ")
animals.remove("dog") # removes dog from the list
animals.append("sheep") # adds sheep to the end of list
animals.pop() # removes the most recent animal in the list
animals.insert(1, "goat") # adds element to the second position in the list

print("\n")
print(animals)
print("Index of element in a list: "+str(animals.index("rabbit"))) # returns index of an element
print("Total count of an element in a list: "+str(animals.count("rabbit")))

animals.reverse() # reverses the list
print(animals)
animals.clear() # clears the list
print(animals)

# List Comprehensions
numbers = [1,2,3,4,5]
square_nums = [x**2 for x in numbers]
print(square_nums)

# Sets
names = {"Truth", "Grey", "Daniel", "Samuel"}
for name in names:
    print("%s" % name, end=" ")
names.remove("Grey") # removes dog from the list
names.add("Nolan") # adds sheep to the end of list
names.pop() # removes the most recent animal in the list
print("\n")
print(names)

# Tuples
# Note: Tuples are immutable
players = ("Ronaldo", "James", "Saka", "James")
for player in players:
    print("%s" % player, end=" ")

print("\n")
print("Index of the Ronaldo in the list: %d" % players.index("Ronaldo"))
print("Total James in the list: %d" % players.count("James"))
print(players)

# Dictionary
marks = {"Truth": 96, "Betty": 83, "John": 87}
for key, value in marks.items():
    print("%s scored %d" % (key, value), end="\n")

marks['Isaac']=  88
print(marks)

# Map, Filter, and Reduce

# using map function
my_numbers = [1,2,3,4,5]
square_numbers = list(map(lambda x: x**2, my_numbers))
print(square_numbers)

# using filter function
even_numbers = list(filter(lambda x: x % 2 ==0, my_numbers))
print(even_numbers)

# using reduce function
from functools import reduce
product = reduce(lambda x, y: x * y, my_numbers)
print(product)