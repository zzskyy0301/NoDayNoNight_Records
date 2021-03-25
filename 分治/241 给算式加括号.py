'''讲解视频https://www.youtube.com/watch?v=gxYV8eZY0eQ
记忆化递归'''
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        #递归出口
        if expression.isdigit():
            return [int(expression)]#这里千万别忘了返回list，并转换int
        calcus=['-','+','*']
        ans=[]
        for i,char in enumerate(expression):
            if char in calcus:
                l=self.diffWaysToCompute(expression[0:i])
                r=self.diffWaysToCompute(expression[i+1:])
                for left in l:
                    for right in r:
                        if char=='+':
                            ans.append(left+right)
                        elif char=='-':
                            ans.append(left-right)
                        elif char=='*':
                            ans.append(left*right)
        return ans


#分支思想，找到递归出口
