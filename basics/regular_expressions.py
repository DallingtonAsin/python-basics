# Regular Expressions
import re

pattern = r"\d+"
string = "hello123world"
match = re.search(pattern, string)
print(match.group())

# Generators
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

_generator = infinite_sequence()
for _ in range(25):
    print("%d" % (next(_generator)), end = " ")


# Decorators
def my_decorator(func):
    def wrapper():
        print("\nSomething is happening before the function is called.")
        func()
        print("Something is happening after the function is called.\n")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

