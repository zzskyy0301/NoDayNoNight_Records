https://leetcode-cn.com/problems/range-sum-query-immutable/submissions/
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.sums=[0]*len(nums)
        self.sums[0]=nums[0]
        for i in range(1,len(nums)):
            self.sums[i]=self.sums[i-1]+nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return self.sums[right]-self.sums[left]+self.nums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
