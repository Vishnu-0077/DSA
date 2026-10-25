class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        hash = {}
        ans = ''
        for i in range(len(s)):
            if s[i] in t:
                hash[s[i]] = i

                if len(hash) == len(t):
                    l = min(hash.values())
                    r = max(hash.values())
                    if (r-l+1) < len(ans) if ans else float('inf'):
                        ans = s[l:r+1]
        return ans


a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
code = a.minWindow(s=s,t=t)
print(code)