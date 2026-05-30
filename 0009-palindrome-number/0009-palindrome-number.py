class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = True
        x = str(x)
        for i in range(len(x)+1):
            if x[i:i+1] != x[len(x)-i-1:len(x)-i]:
                res = False
        return res