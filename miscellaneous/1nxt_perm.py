class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        def nxt_small_great(nums,i):
            if i == len(nums)-2:
                return i+1
            orig = nums[i]
            mini = i+1
            i+=2
            while i<n:
                if nums[i]>orig and nums[i]<nums[mini]:
                    mini = i
                i+=1
            return mini
        n = len(nums)
        j = n-2
        while j>=0 and nums[j]>=nums[j+1]:
            j-=1
        #find next smallest greatest
        if j==-1:
            j+=1
        else:
            mini = nxt_small_great(nums,j)
            nums[j],nums[mini] = nums[mini],nums[j]
            j+=1
        while j<n:
            k = n-2
            while k>=j:
                if nums[k]>=nums[k+1]:
                    nums[k],nums[k+1] = nums[k+1],nums[k]
                k-=1
            j+=1
        return nums 