class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p1 = [1]*len(nums)
        p2 = [1]*len(nums)
        for i in range(1,len(nums)):
            p1[i] = p1[i-1]*nums[i-1]
            p2[-i-1] = p2[-i]*nums[-i]
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = p1[i]*p2[i]
        return ans