from collections import ChainMap

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "turtles": 1}

pets = ChainMap(for_adoption, vet_treatment)
print(pets["dogs"]) # 10
print(pets["horse"]) # KeyError: 'horse'
print(pets) # ChainMap({'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'turtles': 1})
print(pets.maps) # [{'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'turtles': 1}]
print(list(pets.keys())) # ['dogs', 'turtles', 'cats', 'pythons']
print(list(pets.values())) # [10, 1, 7, 3]

# Dictionary like operations
print(pets["cats"]) # 7


for key, value in pets.items():
    print(f"key:{key}, value:{value}")

# Output
# key:dogs, value:10
# key:turtles, value:1
# key:cats, value:7
# key:pythons, value:3