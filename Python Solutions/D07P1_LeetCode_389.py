class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t1=0
        t2=0
        for i in s:
            t1+=ord(i)
        for j in t:
            t2+=ord(j)
        return chr(t2-t1)
