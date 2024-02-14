class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

import unittest

class TestRotate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rotate_1(self):
        nums = [1, 2, 3, 4, 5]
        k = 2
        expected_output = [4, 5, 1, 2, 3]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected_output)

    def test_rotate_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected_output = [3, 99, -1, -100]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected_output)

    def test_rotate_3(self):
        nums = [1, 2]
        k = 3
        expected_output = [2, 1]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected_output)

if __name__ == '__main__':
    unittest.main()
