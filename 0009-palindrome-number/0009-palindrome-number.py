class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))

        for i in range(0, math.ceil(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return(False)
        
        return(True)