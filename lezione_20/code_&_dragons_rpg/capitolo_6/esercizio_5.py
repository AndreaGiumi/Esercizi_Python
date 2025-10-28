def min_coins(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 0
    
    dp = [1000000000] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount]
