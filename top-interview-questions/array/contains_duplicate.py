class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

import unittest

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate_1(self):
        nums = [1, 2, 3, 4, 5, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_contains_duplicate_2(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_contains_duplicate_3(self):
        nums = []
        self.assertFalse(self.solution.containsDuplicate(nums))

if __name__ == "__main__":
    unittest.main()
