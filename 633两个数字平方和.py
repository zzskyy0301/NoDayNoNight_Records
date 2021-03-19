class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        #range 1-c
        a=0
        while a*a<=c:
            l=0
            r=c-a*a
            while l<=r:
                m=(l+r)//2
                if m*m+a*a==c:
                    return True
                elif m*m+a*a>c:
                    r=m-1
                else:
                    l=m+1
            a+=1
        return False    
        
