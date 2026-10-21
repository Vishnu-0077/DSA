class Solution:
    def subarraysWithKDistinct(self, nums, k):
        
        def sol(nums,k):
            l=0
            r=0
            ans = 0
            hash = {}
            while r<len(nums):
                if nums[r] not in hash:
                    hash[nums[r]]=1
                else:
                    hash[nums[r]]+=1

                while len(hash)>k:
                    hash[nums[l]]-=1
                    if hash[nums[l]]==0:
                        del hash[nums[l]]
                    l+=1
                
                ans+=(r+1-l)
                r+=1
            return ans
        
        return sol(nums,k)-sol(nums,k-1)