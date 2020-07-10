n = 10  # can be anything, this is just an example
sum = 0
pie = 3.14
for var in range(1, n, 3):
    j = 1
    print(pie)
    while j < n:
        sum += 1
        j *= 3
print(sum)  # O(1)


# Time Complexity: O(nlogn)
