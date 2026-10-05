class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            matches = True
            for j in range(len(needle)):
                if needle[j] == haystack[i+j]:
                    continue
                else:
                    matches = 0
                    break
            if matches:
                return i
        return -1