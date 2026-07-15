
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod = nums[0]
        segment_start = 0

        for right in range(len(nums) + 1):
            if right == len(nums) or nums[right] == 0:
                if right < len(nums):
                    max_prod = max(max_prod, 0)

                if segment_start < right:
                    prod = 1
                    first_negative = -1
                    last_negative = -1
                    negative_count = 0

                    for i in range(segment_start, right):
                        prod *= nums[i]

                        if nums[i] < 0:
                            negative_count += 1

                            if first_negative == -1:
                                first_negative = i

                            last_negative = i

                    if negative_count % 2 == 0:
                        max_prod = max(max_prod, prod)
                    else:
                        if first_negative + 1 < right:
                            suffix_prod = 1

                            for i in range(first_negative + 1, right):
                                suffix_prod *= nums[i]

                            max_prod = max(max_prod, suffix_prod)

                        if segment_start < last_negative:
                            prefix_prod = 1

                            for i in range(segment_start, last_negative):
                                prefix_prod *= nums[i]

                            max_prod = max(max_prod, prefix_prod)

                        if right - segment_start == 1:
                            max_prod = max(max_prod, nums[segment_start])

                segment_start = right + 1

        return max_prod