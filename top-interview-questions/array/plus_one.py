class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

import unittest

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_increment(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_increment_with_carry(self):
        self.assertEqual(self.solution.plusOne([1, 2, 9]), [1, 3, 0])

    def test_increment_resulting_in_new_digit(self):
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_increment_single_digit(self):
        self.assertEqual(self.solution.plusOne([0]), [1])

    def test_increment_with_zeros(self):
        self.assertEqual(self.solution.plusOne([0, 0, 1]), [0, 0, 2])

    def test_large_number_increment(self):
        self.assertEqual(self.solution.plusOne([9]*10), [1] + [0]*10)

if __name__ == '__main__':
    unittest.main()
