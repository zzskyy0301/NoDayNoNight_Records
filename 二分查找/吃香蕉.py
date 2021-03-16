#第875题目
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        r=max(piles)
        
        while l<r:
            t=0
            m=l+(r-l)//2
            for p in piles:
                t+=(p+m-1)/m
            if t<=h:
                r=m
            else:
                l=m+1
        return l
  
