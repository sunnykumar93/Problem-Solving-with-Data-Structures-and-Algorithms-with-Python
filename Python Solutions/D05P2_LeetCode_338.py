class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        dic={}
        dic[0]="0"
        dic[1]="1"
        if n==0:
            l.append(0)
        else:
            l.append(0)
            l.append(1)
        for i in range(2,n+1):
            n1=i
            rem=n1%2
            n2=n1>>1
            dic[n1]=dic[n2]+str(rem)
            a=dic[n1]
            l.append(a.count("1"))
        
        return l
