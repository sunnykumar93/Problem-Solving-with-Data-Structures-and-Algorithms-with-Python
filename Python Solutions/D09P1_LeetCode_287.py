class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        l=[]
        for i in nums:
            if i in dic:
                l.append(i)
            else:
                dic[i]=1
        return l[0]
