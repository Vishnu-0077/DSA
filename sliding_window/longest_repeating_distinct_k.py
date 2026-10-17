class Solution:
    def kDistinctChar(self, s, k):
        if k==0:
            return 0
        l = 0
        r = 0
        c = 0
        max_c = 0
        hash = {}
        while r<len(s):
            if k!=0 and s[r] not in hash:
                c+=1
                hash[s[r]]=1
                k-=1
                r+=1
            elif k==0 and s[r] not in hash:
                while hash[s[l]]!=0:
                    hash[s[l]]-=1
                    c-=1
                    if hash[s[l]]==0:
                        k+=1
                        del hash[s[l]]
                        l+=1
                        break
                    l+=1
                
                #now adding my boy(next term)
                hash[s[r]] = 1
                c+=1
                k-=1
                r+=1
            else:
                c+=1
                hash[s[r]]+=1
                r+=1

            max_c = max(max_c,c)
        return max_c

p = Solution()
s = "aababbcaacc"
k = 2
gay = p.kDistinctChar(s = s, k = k)
print(gay)