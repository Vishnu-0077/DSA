class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = {}
        ans = s
        for i in range(len(s)):
            if s[i] in t:
                hash[s[i]]=i
            if len(hash)==len(t):
                l = min(hash.values())
                r = max(hash.values())
                if r+1-l<len(ans):
                    ans = s[l:r+1]
        return ans

a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
code = a.minWindow(s=s,t=t)
print(code)