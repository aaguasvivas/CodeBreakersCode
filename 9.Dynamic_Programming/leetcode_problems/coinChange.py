class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]
        dp[0][0] = 0
        firstCoin = coins[0]
        for i in range(amount + 1):
            if i >= firstCoin:
                dp[0][i] = dp[0][i - firstCoin] + 1

        for i in range(1, len(coins)):
            for j in range(amount + 1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        if dp[-1][-1] != float("inf"):
            return dp[-1][-1]
        return -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
