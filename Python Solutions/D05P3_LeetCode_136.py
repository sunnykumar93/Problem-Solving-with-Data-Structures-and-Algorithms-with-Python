# Python3 code coming soon
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            n=n^i
        return n    
