剑指 Offer 10- I. 斐波那契数列
不能用递归 要用动态规划
class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        for i in range(0,n):
            a,b=b,a+b
        return a % 1000000007
