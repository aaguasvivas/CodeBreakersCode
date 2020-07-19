def removeKdigits(nums, k):
    # O(n) time and space
    stack = []

    for num in nums:
        while stack and k and int(stack[-1]) > int(num):
            stack.pop()
            k -= 1
        stack.append(num)

    if k:
        stack = stack[:-k]

    cur = 0
    while cur < len(stack) and stack[cur] == '0':
        cur += 1
    stack = stack[cur:]

    return "".join(stack) or "0"
