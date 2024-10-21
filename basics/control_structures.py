# Control Structures
x = 7
y = 8

level = 5
if 0 < level < 11:
    print("valid")
if level == 5 or level == 7:
    print("special")

# if else if statement
if x > y:
    print("%d is greater than %d" % (x, y))
elif x == y:
    print("%d is equal to %d" % (x, y))
else:
    print("%d is less than %d" % (x, y))

# for loop
for i in range(10):
    print("%d" % i, end=" ")

print("\n")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")

# While loop
num = 0
total = 0
while num < 10:
    total += num
    num += 1
print("\nThe sum of numbers from 0 to 10 is %d" % total)

# Functions
def sum_of_digits(n) -> int:
    _total = 0
    counter = 0
    for _n  in n:
        _total += _n
        counter += 1
    return _total

print("\nSum of numbers in the list using the func is %d" % sum_of_digits({13, 4, 8, 12}))

# Exception Handling
def divide_nums(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Can't divide by zero")

print("\nDivide numbers using the func is %f" % divide_nums(13, 4))

# Anonymous function using lambda
multiple = lambda o,p,q: o * p * q
a,b,c = [1,2,3]
print("\nProduct of %d, %d, %d is %d" % (a, b, c, (multiple(a,b,c))))