class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        i = 0
        substring = ""
        substrings = []

        for j in range(0, len(s)):
            for i in range(j, len(s)):
                current = s[i]

                if current not in substring:
                    substring += current
                else:
                    substrings.append(substring)
                    substring = ""
                    break
            
            substrings.append(substring)

        
        longest = 0

        for k in substrings:
            if len(k) > longest:
                longest = len(k)

        return longest