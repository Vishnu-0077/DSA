class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(nums)):
            if target-nums[i] not in hash:
                hash[nums[i]] = i
            else:
                return [hash[target - nums[i]],i]
        