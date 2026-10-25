def better(s): #when it is a string
    r = s[::-1]
    n = len(s)
    dp = [[0]*n for i in range(n)]
    for i in range(n):
        if r[0]==s[i]:
            dp[0][i]=1
        else:
            dp[0][i] = dp[0][i-1]
    
    for i in range(n):
        if s[0]==r[i]:
            dp[i][0]=1
        else:
            dp[i][0] = dp[i-1][0]
    
    for i in range(1,n):
        for j in range(1,n):
            if s[i] == r[j]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    ans = dp[i][j]
    return n - ans

s = 'abcdadbe'
print(f'when we use a string {better(s)}')

#when we have to merge the operations to make them palindromic then there is ta differnt method

def beeb(arr):
    n = len(arr)
    l = 0
    r = n-1
    ans = 0
    while l<=r:
        if arr[l] == arr[r]:
            l+=1
            r-=1
            
        elif arr[l]<arr[r]:
            l+=1
            arr[l]+=arr[l-1]
            ans+=1
        else:
            r-=1
            arr[r]+=arr[r+1]
            ans+=1
        
    return ans

arr = [1, 4, 5, 1]
print(beeb(arr))

