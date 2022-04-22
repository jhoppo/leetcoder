class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Runtime: 657 ms, faster than 99.63% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.6 MB, less than 10.02% of Python3 online submissions for Maximum Subarray."""
        curSum = maxSum = nums[0]
        for i in nums[1::]:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = curSum if curSum > maxSum else maxSum
        return maxSum