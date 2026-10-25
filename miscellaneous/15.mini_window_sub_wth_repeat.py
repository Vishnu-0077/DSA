class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        hash = {}
        ans = ''
        c = 0
        for x in t:
            if x not in hash:
                hash[x] = 1
            else:
                hash[x]+=1
        l = 0
        r = 0
        while r<len(s):
            if s[r] in hash and hash[s[r]]>=1:
                c+=1
            if s[r] not in hash:
                hash[s[r]] = -1
            else:
                hash[s[r]]-=1
            while c==len(t):
                if not ans or (r+1-l)<len(ans):
                    ans = s[l:r+1]
                hash[s[l]]+=1
                if hash[s[l]]>0:
                    c-=1
                l+=1
            r+=1
        return ans
                