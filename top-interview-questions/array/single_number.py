class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num) == 1:
                return num

import unittest

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_number_1(self):
        nums = [2, 2, 1]
        expected_output = 1
        self.assertEqual(self.solution.singleNumber(nums), expected_output)

    def test_single_number_2(self):
        nums = [4, 1, 2, 1, 2]
        expected_output = 4
        self.assertEqual(self.solution.singleNumber(nums), expected_output)

    def test_single_number_3(self):
        nums = [1]
        expected_output = 1
        self.assertEqual(self.solution.singleNumber(nums), expected_output)

if __name__ == '__main__':
    unittest.main()
