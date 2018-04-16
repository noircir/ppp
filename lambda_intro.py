def square(num): return num * num


# lambda is an anonymous function
# lambda is always one line
square2 = lambda num: num * num

add = lambda a,b: a+b


print(square2(7))
print(add(6,4))

print(square.__name__)
print(square2.__name__)
print(add.__name__)