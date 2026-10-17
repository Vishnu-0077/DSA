class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        hash = {}
        b = 2
        l = 0
        r = 0
        c = 0
        max_c = 0
        while r<len(fruits):
            if b==0 and fruits[r] not in hash:
                hash[fruits[r]] = 1
                c+=1
                r+=1
                b-=1

                while hash[fruits[l]]!=0:
                    hash[fruits[l]] -= 1
                    c-=1
                    if hash[fruits[l]]==0:
                        del hash[fruits[l]]
                        b+=1
                        l+=1
                        break
                    l+=1
                
                
            
            elif fruits[r] not in hash:
                hash[fruits[r]]=1
                c+=1
                b-=1
                r+=1
            
            else:
                hash[fruits[r]]+=1
                c+=1
                r+=1
            max_c = max(c,max_c)
        return max_c