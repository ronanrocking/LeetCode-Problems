class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)

        if s[0] == '-':
            multiplier = -1
            s = s[1:]
        else:
            multiplier = 1
        
        
        rev = s[::-1]

        irev = int(rev)

        if (irev > pow(2, 31)):
            return 0
        
        return(multiplier*irev)
        