class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        l=[]
        for i in height:
            l.append(i)
            left.append(max(l))
        right=[]
        r=[]
        for j in range(len(height)-1,-1,-1):
            r.append(height[j])
            right.insert(0,max(r))
        
        count=0
        

        for i in range(len(height)):
            m=min(left[i],right[i])
            t=m-height[i]
            
            count+=t
            
        return count
