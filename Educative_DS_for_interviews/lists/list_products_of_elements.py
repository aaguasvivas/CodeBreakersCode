def findProduct(lst):
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left *= ele

    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] = product[i] * right
        right *= lst[i]
    return product

# Time Complexity: O(n)
