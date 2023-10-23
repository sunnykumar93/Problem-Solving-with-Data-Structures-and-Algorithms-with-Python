class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic={}
        l=[]
        for i in arr:
            dic[i]=bin(i).count("1")
        
        s=list(set(dic.values()))
        s=sorted(s)
        for i in s:
            k1=[]
            for j in arr:
                if i==dic[j]:
                    k1.append(j)
                k1.sort()
            l+=k1
        

        return l
