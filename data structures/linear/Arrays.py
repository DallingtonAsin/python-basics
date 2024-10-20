# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

numbers = [30, 50, 34, 45]
print("\nElements in the list:")
for x in numbers:
    print("%d" % x, end = ' ')


numbers[0] = 100 # replace the first element in the list
print("\nList after replacing the first element")
for x in numbers:
    print("%d" % x, end = ' ')

numbers.insert(4, 86)  # add an element in the list
print("\nElements after inserting a new value")
for x in numbers:
    print("%d" % x, end = ' ')


numbers.pop(0)  # remove an element from the list
print("\nElements after removing value from the list")
for x in numbers:
    print("%d" % x, end = ' ')