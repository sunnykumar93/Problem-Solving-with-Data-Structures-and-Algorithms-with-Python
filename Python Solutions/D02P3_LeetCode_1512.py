class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        count=0
        for k,v in dic.items():
            a=(v*(v-1))//2
            count+=a
        return count
