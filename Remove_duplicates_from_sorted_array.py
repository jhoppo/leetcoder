"""
Runtime: 212 ms, faster than 13.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 66.06% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            counts = nums.count(num)
            if counts == 1: continue
            for i in range(1, counts):
                nums.remove(num)
        return len(nums)
