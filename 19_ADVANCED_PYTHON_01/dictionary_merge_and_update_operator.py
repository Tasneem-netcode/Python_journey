dict1 = {"a":1 , "b" : 2}
dict2 = {"b":3 , "c" : 6}
merge = dict1 | dict2

print(merge)


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1 |= dict2
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
