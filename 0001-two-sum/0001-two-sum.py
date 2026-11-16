class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen :
                return [seen[needed], i]
            seen[num] = i
        return []
        # left = 0
        # right = len(nums) - 1

        # while left < right :
        #     total = nums[left] + nums [right]


        #     if total == target:
        #         return [left, right]

        #     elif total > target:
        #         right -= 1
            
        #     else:
        #         left += 1
        # return []