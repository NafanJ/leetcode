import unittest

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts = {}
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
    
        # Find the intersection with nums2
        intersection = []
        for num in nums2:
            if num in counts and counts[num] > 0:
                intersection.append(num)
                counts[num] -= 1
                if counts[num] == 0:
                    del counts[num]
    
        return intersection

class TestIntersect(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_arrays(self):
        self.assertEqual(self.solution.intersect([], []), [])

    def test_no_intersection(self):
        self.assertEqual(self.solution.intersect([1, 2, 3], [4, 5, 6]), [])

    def test_single_element_intersection(self):
        self.assertEqual(self.solution.intersect([1], [1]), [1])

    def test_multiple_elements_intersection(self):
        self.assertEqual(sorted(self.solution.intersect([1, 2, 2, 1], [2, 2])), [2, 2])

    def test_subset_intersection(self):
        self.assertEqual(sorted(self.solution.intersect([1, 2, 2, 1], [1, 1, 2])), [1, 1, 2])

    def test_mixed_numbers_intersection(self):
        self.assertEqual(sorted(self.solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])), [4, 9])

    def test_large_numbers_intersection(self):
        self.assertEqual(sorted(self.solution.intersect([10, 10, 10], [10, 10])), [10, 10])

    def test_duplicate_numbers_in_both_arrays(self):
        self.assertEqual(sorted(self.solution.intersect([8, 0, 3, 12, 0], [8, 8, 0])), [0, 8])

if __name__ == "__main__":
    unittest.main()
