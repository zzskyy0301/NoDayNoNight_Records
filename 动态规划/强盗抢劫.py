#题目地址https://leetcode-cn.com/problems/house-robber/submissions/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            opt=[0]*len(nums)
            opt[0]=nums[0]
            opt[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):#0,1,2,3,4
                opt_s=opt[i-2]+nums[i]
                opt_n=opt[i-1]
                if opt_s>=opt_n:
                    opt[i]=opt_s
                else:
                    opt[i]=opt_n
            return opt[len(nums)-1]
