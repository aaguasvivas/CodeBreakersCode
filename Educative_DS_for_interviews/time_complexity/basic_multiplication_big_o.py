n = 10  # n can be anything, this is just an example
sum = 0
pie = 3.14
var = 1
while var < n:
    print(pie)
    for j in range(1, n, 2):
        sum += 1
    var *= 3
print(sum)


# Time Complexity: O(nlogn)
