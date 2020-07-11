# Join, Split
# Dictionaries
# 1. Hashable vs unhashable
# 2. Sets

# Join, Split
words = ["This", "is", "a", "sentence"]
new_string = " ".join(words)
print(new_string)

lst = new_string[:].split()
print(lst)

# Dictionaries
d = {key: key*2 for key in range(11)}
print(d)

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
myDict = {k: v for k, v in zip(keys, values)}
print(myDict)

print(2 in d)
d[3] = 10
print(d)

for key in d.keys():
    print(key)

for key, value in d.items():
    print((key, value))

# Sets
my_set = set()
my_set.add(1)
print(1 in my_set)
my_set.add(2)
my_set.add((1, 2))
print(my_set)

arr = [1, 2, 3, 4, 3]
my_set = set()

for num in arr:
    if num in my_set:
        print("Found duplicate!")
    else:
        my_set.add(num)
