class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        for i in str(n):
            s+=int(i)
            m*=int(i)
        return m-s
