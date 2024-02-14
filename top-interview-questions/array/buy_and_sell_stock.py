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

# Import the unittest module
import unittest

# Define a test case class that inherits from unittest.TestCase
class TestMaxProfit(unittest.TestCase):
    def test_example(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([7,1,5,3,6,4]), 7, "The max profit should be 7")

    def test_no_profit(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([7,6,4,3,1]), 0, "The max profit should be 0")

    def test_increasing_prices(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([1,2,3,4,5]), 4, "The max profit should be 4")

    def test_empty_list(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([]), 0, "The max profit should be 0")

    def test_single_element(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([5]), 0, "The max profit should be 0")

# This allows the test cases to be executed when the script is run directly
if __name__ == '__main__':
    unittest.main()
