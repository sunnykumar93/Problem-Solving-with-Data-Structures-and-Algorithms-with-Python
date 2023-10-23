class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        l.append([])
        for i in nums:
            k=[]
            for j in l:
                k.append(j+[i])
            l+=k    
        return l
            
