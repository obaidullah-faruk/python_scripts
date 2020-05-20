from collections import Counter

name = "aaaaaaaaabbbcc"
my_counter = Counter(name)
print(my_counter)
print(f"Most common:  {my_counter.most_common(1)}")
print(f"Most common:  {my_counter.most_common(1)[0]}")
print(f"Most common:  {my_counter.most_common(1)[0][0]}")
print("Items: ", my_counter.items())
print("Keys: ", my_counter.keys())
print("Values", my_counter.values())
print("-------------")
print(my_counter.elements())
print(list(my_counter.elements()))