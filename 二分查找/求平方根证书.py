#69
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l=0
        r=x+1
        while l<r:
            m=l+(r-l)//2
            if m*m>x:
                r=m
            else:
                l=m+1 #l是大于平方根的整数，要返回l-1!
        return l-1
