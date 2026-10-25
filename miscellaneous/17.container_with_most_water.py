class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxi = 0
        while l<r:
            vol = min(height[l],height[r])*(r-l)
            maxi = max(maxi,vol)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi

        