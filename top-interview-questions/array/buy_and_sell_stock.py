class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
                
if __name__ == "__main__":
    solution = Solution()

    print("Test Case 1")
    prices = [7,1,5,3,6,4,2,4]
    profit = solution.maxProfit(prices)
    print("Maximum proift:", profit)