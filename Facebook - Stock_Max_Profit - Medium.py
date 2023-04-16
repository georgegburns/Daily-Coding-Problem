# Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. 
# You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

def maxProfit(lst : list, k : int):
    prices = []
    for i, price1 in enumerate(lst):
        for price2 in lst[i+1:]:
            diff = price2 - price1
            prices.append(diff)
    prices.sort(reverse=True)
    profit = sum(prices[:k])
    return profit

TEST = [5, 2, 4, 0, 1]
k = 3

print(maxProfit(TEST, k))