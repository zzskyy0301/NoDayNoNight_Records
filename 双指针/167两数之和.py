#方法一：双指针 缩小查找范围
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return i+1,j+1
            if numbers[i]+numbers[j]<target:
                i+=1
            if numbers[i]+numbers[j]>target:
                j-=1
        return i+1,j+1
     #方法二：二分查
     class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            l=i+1
            r=len(numbers)-1
            while l<=r:
                m=(l+r)//2
                if numbers[i]+numbers[m]==target:
                    return i+1,m+1
                if numbers[i]+numbers[m]>target:
                    r=m-1
                else:
                    l=m+1
        return [-1,-1]
      
