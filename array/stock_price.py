def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_price = 0
    min_price = float("inf")

    i, j = 0, 1
    while j < len(prices):

        if prices[i] < min_price:
            min_price = prices[i]

        if prices[j] > max_price:
            max_price = prices[j]

        i += 1
        j += 1
        print(max_price)
        print(min_price)
        print("\n")

    return max_price - min_price

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
