# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def stock(self,prices):
        n=len(prices)
        min_price=prices[0]
        profit=0

        for i in range (1,n):
            current_profit=prices[i]-min_price
            if current_profit>profit:
                profit=current_profit
            min_price=min(min_price,prices[i])

        return profit


prices=list(map(int,input("Enter  price of a  stock on the ith day: ").split()))
obj=Solution()
result=obj.stock(prices)
print(result)