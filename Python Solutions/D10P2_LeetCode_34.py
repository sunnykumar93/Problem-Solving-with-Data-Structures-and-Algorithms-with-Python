class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[-1,-1]
        low=0
        high=len(nums)-1
        low_bound=len(nums)
        h_bound=len(nums)
        if target not in nums:
            return l
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                low_bound=mid
                high=mid-1
            else:
                low=mid+1

        print(low_bound)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                h_bound=mid
                high=mid-1
            else:
                low=mid+1
        print(h_bound-1)
        l=[low_bound,h_bound-1]
        return l
