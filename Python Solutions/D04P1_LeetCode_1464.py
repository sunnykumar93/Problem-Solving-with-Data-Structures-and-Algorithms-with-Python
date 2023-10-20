class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=0
        m2=0
        for i in nums:
            if m<=i:
                temp=m
                m=i
                m2=temp
            elif m2<=i:
                m2=i
        return (m-1)*(m2-1)
