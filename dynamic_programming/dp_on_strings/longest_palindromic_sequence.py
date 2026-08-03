def tabulation(s):
    sr = s[::-1]
    dp = [[0]*len(s) for _ in range(len(s))]
    if s[0]==sr[0]:
        dp[0][0] = 1
    for i in range(1,len(s)):
        if s[i]==sr[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]
    for j in range(1,len(sr)):
        if sr[j]==s[0]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j-1]


    for i in range(1,len(s)):
        for j in range(1,len(sr)):
            if s[i]==sr[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(s)-1][len(sr)-1]


s = "bbbab"
print(tabulation(s))