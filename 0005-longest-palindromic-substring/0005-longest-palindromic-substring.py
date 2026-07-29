class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        bestL = 0
        bestR = 0

        for start in range(len(s)):
            # Odd-length palindrome
            L = start - 1
            R = start + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1

            if R - L - 1 > bestR - bestL + 1:
                bestL = L + 1
                bestR = R - 1

            # Even-length palindrome
            L = start
            R = start + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1

            if R - L - 1 > bestR - bestL + 1:
                bestL = L + 1
                bestR = R - 1

        return s[bestL:bestR + 1]