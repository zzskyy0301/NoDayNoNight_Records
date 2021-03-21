class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1) #dp[i]是整数i划分之后最大乘积
        dp[0]=0
        dp[1]=1
        for i in range(0,n+1):#算从0到n的所有数字的dp，然后才能知道n的dp
            for part1 in range(i):
                part2=i-part1
                dp[i]=max(dp[i],dp[part2]*part1,part2*part1)
                #print(i,part1,dp[i])
        return dp[n]
