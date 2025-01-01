from collections import ChainMap

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

# Create a ChainMap
merged = ChainMap(numbers, letters)
print(merged["b"]) # Output: B


# merged["three"] # KeyError: 'three'


# in case of duplicate keys, the value from the first dictionary is used
# also applies to iteration

# mutation is allowed, in case of duplicate keys, the value is updated in the first dictionary



for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "turtles": 1}

pets = ChainMap(for_adoption, vet_treatment)
print(pets) # ChainMap({'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'turtles': 1})
print(pets.maps) # [{'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'turtles': 1}]