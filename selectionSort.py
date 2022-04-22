# class Solution:
#     def SelectionSort(self, s: str, words: List[str]) -> List[int]:
def SelectionSort(nums, reverse=0):
    for i in range(len(nums)):
        limit_ind = i
        for j in range(i+1, len(nums)):
            if reverse == 0:
                if nums[j] < nums[limit_ind]: limit_ind = j
            elif reverse == 1:
                if nums[j] > nums[limit_ind]: limit_ind = j
            else:
                return False

        nums[i], nums[limit_ind] = nums[limit_ind], nums[i]
    return nums
