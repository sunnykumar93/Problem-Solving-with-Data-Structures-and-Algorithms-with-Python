class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        n=len(rating)
        left=[0]
        right=[0]
        for i in range(1,n):
            count=0
            for j in range(0,i):
                if rating[i]>rating[j]:
                    count+=1
            left.append(count)
        
        for i in range(n-2,-1,-1):
            count=0
            for j in range(n-1,i,-1):
                if rating[i]>rating[j]:
                    count+=1
            right.insert(0,count)
        
        res=0
        for i in range(1,n):
            for j in range(0,i):
                if rating[i]>rating[j]:
                    res+=left[j]
        
        for i in range(n-2,-1,-1):
            for j in range(n-1,i,-1):
                if rating[i]>rating[j]:
                    res+=right[j]
        return res
                    
                    
