#https://leetcode-cn.com/problems/house-robber-ii/submissions/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        else:
            nums_y=nums[0:-1]
            nums_n=nums[1:]
            opty=[0]*len(nums_y)
            optn=[0]*len(nums_n)
            opty[0]=nums_y[0]
            opty[1]=max(nums_y[0],nums_y[1])
            optn[0]=nums_n[0]
            optn[1]=max(nums_n[0],nums_n[1])
            # opt_no=[0]*n
            # opt_yes=opt_no
            # opt_no[0]=0
            # opt_no[1]=nums[1]
            # opt_yes[0]=nums[0]
            # opt_yes[1]=max(nums[0],nums[1])
            for i in range(2,len(nums_n)):
                steal=optn[i-2]+nums_n[i]
                nosteal=optn[i-1]
                optn[i]=max(steal,nosteal)
            for i in range(2,len(nums_y)):
                #print(i)
                    steal=opty[i-2]+nums_y[i]
                    nosteal=opty[i-1]
                    opty[i]=max(steal,nosteal)
            #print(opt_yes[n-1],opt_no[n-1])
        return max(opty[len(nums_y)-1],optn[len(nums_n)-1])
