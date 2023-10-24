class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left=[]
        m=nums[0]
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            m=max(s,m)
            if s<0:
                s=0
            
        return m
