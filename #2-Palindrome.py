class Solution:
    def isPalindrome(self, x: int) -> bool:
        convertedNum = str(x)
        convertedNum  = convertedNum[::-1]
        if str(x) == convertedNum:
            return True
        else: return False
        