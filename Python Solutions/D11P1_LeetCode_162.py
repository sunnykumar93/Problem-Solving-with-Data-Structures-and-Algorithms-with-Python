class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        ans=0
        while(low<=high):
            mid=(low+high)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                ans=mid
                break
            elif nums[mid]<nums[mid+1]:
                low=mid+1
            elif nums[mid-1]>nums[mid]:
                high=mid-1
        return ans
