class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=float("inf")
        if len(nums)==1:
            return nums[0]
        
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
            
               
        return ans
