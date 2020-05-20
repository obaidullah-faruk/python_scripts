def location_check(x, y):
    if id(y) == id(x):
        print("x and y are sharing the same memory location: ", id(x))
    else:
        print("x and y are not sharing the same memory location: ", id(x), id(y))

x = 10
print(type(x))
y = x

location_check(x, y)

x = x + 1
location_check(x, y)

# x = 4
# print(id(x))
# x = x + 1
# print(id(x))

# Stack Memory and Heap Memory