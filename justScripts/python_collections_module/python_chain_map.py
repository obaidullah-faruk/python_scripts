from collections import ChainMap

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }

chain_map = ChainMap(dict1, dict2)

print(f"{type(chain_map)}")
print(f"{chain_map}")

print(f"{chain_map['a']}")
print(f"{chain_map['c']}")

chain_map['c'] = 9
print(f"{chain_map}")

print(f"{list(chain_map.keys())}")
print(f"{list(chain_map.values())}")

dict3 = {'e' : 5, 'f' : 6}

chain_map = chain_map.new_child(dict3)
print(f"{chain_map}")
