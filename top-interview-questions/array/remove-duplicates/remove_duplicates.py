class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    nums = [1, 1, 2]
    print("Original list:", nums)
    new_length = solution.removeDuplicates(nums)
    print("Modified list after removing duplicates:", nums[:new_length])
    print("New length of the list:", new_length)