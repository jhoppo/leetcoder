import PalidromeNumber
if __name__ == '__main__':
    res = PalidromeNumber.Solution.isPalindrome(x=393)
    print(res)

nums = [3,3,2]
val = 3
j = 0
for num in nums:
    if num != val:
        nums[j] = num
        j+=1
print(nums)