n = 10  # can be anything
sum = 0
pie = 3.14
j = 1
for var in range(n):
    while j < var:
        sum += 1
        j *= 2
    print(sum)


# Time Complexity: O(n)
