def maxProfit(prices):

  left = 0
  right = len(prices) - 1

  max_profit = 0
  while(left < right): #O(n)

    while(prices[left] > prices[right]):
      left += 1

    for i in range(right , left , -1):
      profit = prices[i] - prices[left]

      if profit > max_profit:
        max_profit = profit

    left += 1
  return max_profit


prices = [7,1,5,3,6,4]

print(maxProfit(prices))
    