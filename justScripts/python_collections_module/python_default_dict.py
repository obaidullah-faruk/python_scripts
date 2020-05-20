from collections import defaultdict

my_dictionary = defaultdict(list)

my_dictionary['a'] = 4
my_dictionary['c'] = 45

print(f"{my_dictionary}")
print(f"a: {my_dictionary['a']}")
print(f"Not exist: {my_dictionary['bsd']}")


