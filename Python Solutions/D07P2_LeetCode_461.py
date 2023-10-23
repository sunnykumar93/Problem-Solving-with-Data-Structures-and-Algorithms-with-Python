class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1=bin(x)
        x1=x1[2:]
        print(x1)
        y1=bin(y)
        y1=y1[2:]
        print(y1)
        l=0
        if len(x1)>len(y1):
            l=len(x1)-len(y1)
            y1="0"*l+y1
        else:
            l=len(y1)-len(x1)
            x1="0"*l+x1
        
        count=0
        for i in range(len(x1)):
            if x1[i]!=y1[i]:
                count+=1

        return count
