import unittest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        return max_length

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring_abcabcbb(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_lengthOfLongestSubstring_bbbbb(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_lengthOfLongestSubstring_pwwkew(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_lengthOfLongestSubstring_aab(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aab"), 2)

    def test_lengthOfLongestSubstring_dvdf(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("dvdf"), 3)

    def test_lengthOfLongestSubstring_space(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(" "), 1)

    def test_lengthOfLongestSubstring_empty(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

if __name__ == '__main__':
    unittest.main()
