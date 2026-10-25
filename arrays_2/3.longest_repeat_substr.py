class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        l = 0
        r = 0
        c = 0
        maxi = 0
        while r<len(s):
            while s[r] in hash:
                hash[s[l]]-=1
                if hash[s[l]]==0:
                    del hash[s[l]]
                c-=1
                l+=1
            hash[s[r]]=1
            c+=1
            maxi = max(maxi,c)
            r+=1
        return maxi
        