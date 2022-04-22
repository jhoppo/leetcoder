class FindLimit:
    def __init__(self, nums):
        self.nums = nums
    def FindMin(self):
        minNum = self.nums[0]
        for i in self.nums:
            if i < minNum:
                minNum = i
        return minNum

    def FindMax(self):
        maxNum = self.nums[0]
        for i in self.nums:
            if i > maxNum:
                maxNum = i
        return maxNum