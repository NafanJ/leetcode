class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) == 0:
            return i
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        new_length = solution.removeDuplicates(nums)
        self.assertEqual(new_length, len(expected_nums), "Incorrect new length returned")
        self.assertEqual(nums[:new_length], expected_nums, "The list was not modified correctly")

    def test_example_2(self):
        solution = Solution()
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected_nums = [0,1,2,3,4]
        new_length = solution.removeDuplicates(nums)
        self.assertEqual(new_length, len(expected_nums), "Incorrect new length returned")
        self.assertEqual(nums[:new_length], expected_nums, "The list was not modified correctly")

    def test_empty_list(self):
        solution = Solution()
        nums = []
        expected_nums = []
        new_length = solution.removeDuplicates(nums)
        self.assertEqual(new_length, len(expected_nums), "Incorrect new length returned for an empty list")
        self.assertEqual(nums, expected_nums, "The list was not modified correctly for an empty list")

    def test_single_element(self):
        solution = Solution()
        nums = [1]
        expected_nums = [1]
        new_length = solution.removeDuplicates(nums)
        self.assertEqual(new_length, len(expected_nums), "Incorrect new length returned for a single-element list")
        self.assertEqual(nums, expected_nums, "The list was not modified correctly for a single-element list")

    def test_all_identical_elements(self):
        solution = Solution()
        nums = [5, 5, 5, 5]
        expected_nums = [5]
        new_length = solution.removeDuplicates(nums)
        self.assertEqual(new_length, len(expected_nums), "Incorrect new length returned for a list of all identical elements")
        self.assertEqual(nums[:new_length], expected_nums, "The list was not modified correctly for a list of all identical elements")

if __name__ == '__main__':
    unittest.main()
