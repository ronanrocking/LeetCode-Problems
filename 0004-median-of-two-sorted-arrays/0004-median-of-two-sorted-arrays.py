class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 == 0:
            d1 = nums[int(len(nums)/2)]
            d2 = nums[int(len(nums)/2 - 1)]

            return float((d1+d2)/2)

        else:
            return float((nums[len(nums)//2]))