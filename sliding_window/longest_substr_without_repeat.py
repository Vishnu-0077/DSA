class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxi = 0
        max_f = 0
        hash = {}
        while r<len(s):
            if s[r] not in hash:
                hash[s[r]]=1
            else:
                hash[s[r]]+=1
            max_f = max(max_f,hash[s[r]])
            change = (r+1-l) - max_f
            while change>k:
                hash[s[l]]-=1
                l+=1
                change = (r+1-l) - max(hash.values())
            else:
                maxi = max(maxi,r+1-l)
                r+=1
                
        return maxi

s = "BAABAABBBAAA"
k = 2
p = Solution()
code = p.characterReplacement(s=s,k=k)
print(code)