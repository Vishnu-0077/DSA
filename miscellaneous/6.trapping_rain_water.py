class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        low = 0
        high = n-1
        ans = 0
        prev_low = 0
        prev_high = n-1
        while low<high:
            if height[low]<height[high]:
                if height[low]>height[prev_low]:
                    prev_low = low
                else:
                    ans+=(height[prev_low]-height[low])
                low+=1
            else:
                if height[high]>height[prev_high]:
                    prev_high = high
                else:
                    ans+=(height[prev_high] - height[high])
                high-=1
        return ans
            
            
