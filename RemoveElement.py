class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Runtime: 49 ms, faster than 42.16% of Python3 online submissions for Remove Element.
Memory Usage: 14 MB, less than 15.03% of Python3 online submissions for Remove Element."""
        if len(nums) == 0: return 0
        l ,r = 0, len(nums)-1
        if l == r:
            if nums[l] == val:
                return 0
            else:
                return 1
        while l<r:
            while nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
                if r < l : break
            l+=1
        r = r if nums[r] == val else r+1
        if r < 0: r = 0
        return r
class Solution2:
    def removeElement(selfself, nums: List[int], val: int) -> int:
        """Runtime: 40 ms, faster than 66.57% of Python3 online submissions for Remove Element.
Memory Usage: 13.9 MB, less than 15.03% of Python3 online submissions for Remove Element."""
        j = 0
        for i in nums:
            if not i == val:
                nums[j] = i
                j+=1
        return j