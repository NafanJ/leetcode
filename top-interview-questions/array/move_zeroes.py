class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap only if i and lastNonZeroFoundAt are different
                if i != lastNonZeroFoundAt:
                    nums[i], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[i]
                lastNonZeroFoundAt += 1

import unittest

class TestMoveZeroes(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        arr = [0,1,0,3,12]
        solution.moveZeroes(arr)
        self.assertEqual(arr, [1,3,12,0,0])

    def test_all_zeros(self):
        solution = Solution()
        arr = [0, 0, 0, 0]
        solution.moveZeroes(arr)
        self.assertEqual(arr, [0, 0, 0, 0])

    def test_no_zeros(self):
        solution = Solution()
        arr = [1, 2, 3, 4]
        solution.moveZeroes(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_zeros_at_start(self):
        solution = Solution()
        arr = [0, 0, 1, 2, 3]
        solution.moveZeroes(arr)
        self.assertEqual(arr, [1, 2, 3, 0, 0])

    def test_zeros_in_middle(self):
        solution = Solution()
        arr = [1, 0, 2, 0, 3]
        solution.moveZeroes(arr)
        self.assertEqual(arr, [1, 2, 3, 0, 0])

    def test_alternating_zeros(self):
        solution = Solution()
        arr = [0, 1, 0, 2, 0, 3]
        solution.moveZeroes(arr)
        self.assertEqual(arr, [1, 2, 3, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
