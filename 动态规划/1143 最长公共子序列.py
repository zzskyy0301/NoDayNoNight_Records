class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1)==0 or len(text2)==0:
            return 0
        l1=len(text1)
        l2=len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]#注意dp是怎么定义的
        for i in range(1,l1+1,1): #
            for j in range(1,l2+1,1):
                #print(i,j)
                if text1[i-1]==text2[j-1]:
                    #print(i-1,j-1,dp[i-1][j-1])
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    #print('pickmax')
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                #print(i,j,dp[1][3])
        return dp[i][j]

        # m, n = len(text1), len(text2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if text1[i - 1] == text2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # return dp[-1][-1]


        #注意
