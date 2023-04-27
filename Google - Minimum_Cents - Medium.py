# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.


def minCoins(n : int):
    coins = [25, 10, 5, 1]
    count = 0
    for i in coins:
        if i <= n:
            k = n // i
            n = n % i
            count += k
        if n == 0:
            break
    return count

# O(n) time n(1) space, returns 3 PASS
print(minCoins(16))
