class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        else:
            a1=-1
            a2=-1
            l=0
            r=len(nums)-1
            while l<r:
                m=(l+r)//2
                if nums[m]>=target:
                    r=m
                else:
                    l=m+1
            if nums[l]==target:a1=l
            else:pass
            l=0
            r=len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            
            if nums[l-1]==target:a2=l-1 #要返回right，不是left！最后一轮left和right重合的时候，设置l=m+1,所以要返回right（或者left-1）
            else:pass
            
        return [a1,a2]
