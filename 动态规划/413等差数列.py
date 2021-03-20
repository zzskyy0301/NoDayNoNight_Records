class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return 0
        dp=[0]*len(nums)
        dp[0]=0
        dp[1]=0
        sums=0
        for i in range(2,len(nums)):
            if (nums[i]-nums[i-1])==(nums[i-1]-nums[i-2]):
                dp[i]=dp[i-1]+1
                sums+=dp[i]
            else:
                dp[i]=dp[i]
            #print(i,dp[i])
        return sums
