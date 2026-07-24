class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        i = 0
        while (i < len(nums)):
            if (i > maxIndex):
                return False

            jumpDist = nums[i]
            index = i + jumpDist
            maxIndex = max(maxIndex, index)

            if (maxIndex >= len(nums)-1):
                return True
            
            
            
            i +=1
            
        return False