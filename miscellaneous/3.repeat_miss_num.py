class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hash = {}
        for i in range(1,len(A)+1):
            hash[i] = 0
        for x in A:
            hash[x]+=1
        ans = []
        for x in hash:
            if hash[x]==2:
                ans.append(x)
        for x in hash:
            if hash[x]==0:
                ans.append(x)
                
        return ans
                
