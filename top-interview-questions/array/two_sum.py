import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum_first_example(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_twoSum_second_example(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_twoSum_third_example(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()
