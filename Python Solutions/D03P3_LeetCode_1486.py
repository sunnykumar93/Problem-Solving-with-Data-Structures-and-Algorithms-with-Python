class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=[]
        i=0
        a=0
        while i<n:
            l.append(start+2*i)
            i+=1
        for i in l:
            a=a^i
        return a
