from collections import deque

my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

print(my_deque)

my_deque.appendleft("left")
print(my_deque)
my_deque.pop()
print(my_deque)
my_deque.extendleft(["hello", "hi", "bye"])
print(my_deque)

my_deque.clear()
print(my_deque)