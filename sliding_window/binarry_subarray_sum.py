class Solution:
    def numSubarraysWithSum(self, nums, goal):

        def gay(nums,goal):
            if goal<0:
                return 0
            l = 0
            r = 0
            cur = 0
            c = 0
            while r<len(nums):
                cur+=nums[r]
                while cur>goal:
                    cur-=nums[l]
                    l+=1
                c+=(r+1-l)
                r+=1
            return c
        
        return gay(nums,goal)-gay(nums,goal-1)

s = Solution()
nums =  [1, 1, 0, 1, 0, 0, 1]
goal = 3
code = s.numSubarraysWithSum(nums= nums, goal = goal)
print(code)