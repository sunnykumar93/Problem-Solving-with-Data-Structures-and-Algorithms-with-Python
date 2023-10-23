class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=max(nums)
        s=m*(m+1)//2
        s1=sum(nums)
        d=s-s1
        if d==0:
            if 0 in nums:
                return m+1
            else:
                return 0
        else:
            return d
