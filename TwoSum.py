class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 7594 ms, faster than 5.00% of Python3 online submissions for Two Sum.
        Memory Usage: 15 MB, less than 77.51% of Python3 online submissions for Two Sum.
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            for j in nums[i+1::]+nums[:i:]:
                if nums[i]+j == target:
                    j_ind = nums.index(j)
                    if j_ind == i:
                        j_ind = nums[i+1::].index(j)
                    else:
                        return [i,j_ind]