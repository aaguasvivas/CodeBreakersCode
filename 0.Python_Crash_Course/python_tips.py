# 1. Basic List Functionality
#a. add/pop
#b. indexing
#c. search
#d. iteration

# 2. List Comprehension
# 3. Sorting
# 4. Zip and Enumerate

# Append and pop
lst = []
lst.append(1)
lst.append(2)

for i in range(3, 10):
    lst.append(i)

print(lst.pop())

# List slicing
print(lst[3])
print(lst[3:6])
print(lst[3:])
print(lst[:])
print(lst[:-1])
print(lst[:5:2])
print(lst[::-1])

# Search
print(4 in lst)
print(10 in lst)
lst.index(4)

# Iteration
print(sum(lst))
for i in lst:
    print(i)
count = 0
for i in lst:
    count += 1

s = "abcdef"
for c in s:
    print(c)

# List Comprehension
lst = [i for i in range(1, 9)]

lst = [1] * 10
lst = [[1] * 10 for _ in range(4)]
lst[0][0] = 10

# Sorting
lst = [i for i in range(10, -1, -1)]
lst.sort()  # nlogn
lst = [i for i in range(10, -1, -1)]
copy_lst = sorted(lst)  # Sorted copies list
copy_lst.sort(reverse=True)

# Enumerate
for i, num in enumerate(lst):
    print(i, num)

# Zip
for num1, num2 in zip(lst, copy_lst):
    print(num1, num2)
