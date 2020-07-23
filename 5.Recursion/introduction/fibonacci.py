# O(2^n) time
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(n) time and space


def fibonacciMemo(n, d, memo):
    if n in memo:
        return memo[n]
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

    if n == 0 or n == 1:
        return 1
    current_n = fibonacciMemo(n - 1, d, memo) + fibonacci(n - 2, d, memo)
    memo[n] = current_n
    return current_n

# O(n) time and O(n) space


def fibonacciBottomUp(n):
    dp = [0] * n + 1
    dp[0] = dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


if __name__ == '__main__':
    for i in range(0, 12):
        print(fibonacci(i))
