class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        res=0
        while l<=h:
            m=(l+h)//2
            if m*m>x:
                h=m-1
            elif m*m<=x:
                res=m
                l=m+1
           
        return res
        
