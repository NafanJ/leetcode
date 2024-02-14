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
    print("Test Case 1")
    nums = [1, 1, 2]
    print("Original list:", nums)
    new_length = solution.removeDuplicates(nums)
    print("Modified list after removing duplicates:", nums[:new_length])
    print("New length of the list:", new_length)
    print("Test Case 2")
    nums = [0,0,1,1,1,2,2,3,3,4]
    print("Original list:", nums)
    new_length = solution.removeDuplicates(nums)
    print("Modified list after removing duplicates:", nums[:new_length])
    print("New length of the list:", new_length)