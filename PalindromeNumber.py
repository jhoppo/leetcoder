class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Runtime: 238 ms, faster than 5.03% of Python3 online submissions for Palindrome Number.
    Memory Usage: 13.9 MB, less than 62.56% of Python3 online submissions for Palindrome Number."""
        print(x)
        if x < 0:
            return False

        r2l = 0
        digit = 0
        while 10 ** digit <= x:
            d, m = divmod(x, 10 ** (digit + 1))
            m //= 10 ** digit
            r2l = r2l * 10 + m
            digit += 1
        if r2l == x:
            return True
        else:
            return False
