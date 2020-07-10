def removeEven(num_list):
    return [item for item in num_list if item % 2 != 0]


ten_list = list(range(10))
print(ten_list)
print(removeEven(ten_list))
