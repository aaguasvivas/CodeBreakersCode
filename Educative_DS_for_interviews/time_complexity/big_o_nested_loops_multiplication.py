n = 10  # Can be anything
sum = 0
pie = 3.14
var = 1
while var < n:  # O(logn)
    print(pie)
    for j in range(var):  # O(n)
        sum += 1
    var *= 2
print(sum)


# Time Comlexity: O(n + logn) which is just O(n), we drop lower terms
