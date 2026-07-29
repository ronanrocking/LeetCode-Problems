class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(0, len(nums)):
            num = nums[i]
            complement = target - num

            if complement in dic:
                return list((i, dic[complement]))
            else:
                dic[num] = i