class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if (nums==None or len(nums)==0): return []
        l=0
        r=len(nums)-1
        k=len(nums)-k
        while (l<=r):
            mid=self.quick_sort(nums,l,r)
            if mid==k:
                return nums[k]
            elif mid>k:
                r=mid-1
            else:
                l=mid+1
        return nums[k]

    def quick_sort(self,nums,l,r):
        pivot=nums[r]
        i=l-1
        for j in range(l,r):
            if (nums[j]<pivot):
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        nums[i+1],nums[r]=nums[r],nums[i+1]
        return i+1

作者：geng-chen-i
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/pythonkuai-pai-by-geng-chen-i-uo9c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
