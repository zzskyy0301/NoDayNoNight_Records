#744
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # l=0
        # r=len(letters)-1
        # while l<r:
        #     m=l+(l-r)//2
        #     if letters[m]>target:
        #         r=m
        #     else:
        #         l=m+1
        # if l==len(letters):
        #     return letters[0]
        # else:
        #     return letters[l]
        length = len(letters)
        left = 0
        right = length-1
        while(left<=right):
            mid = (left+right)//2
            if letters[mid]>target:
                right = mid-1
            else:
                left = mid+1
        if left == length:
            return letters[0]
        else:
            return letters[left]
