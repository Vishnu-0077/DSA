class Solution:
    def numberOfOddSubarrays(self, nums, k):
        
        def sol(nums,k):
            l = 0
            r = 0
            cur = 0
            ans = 0
            while r<len(nums):
                if nums[r]%2==1:
                    cur+=1
                while cur>k:
                    if nums[l]%2==1:
                        cur-=1
                    l+=1
                ans+=(r+1-l)
                r+=1
            return ans
        
        return sol(nums,k)-sol(nums,k-1)