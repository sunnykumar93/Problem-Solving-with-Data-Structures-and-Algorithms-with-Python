class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            l=[]
            l=list(range(startTime[i],endTime[i]+1))
            if  queryTime in l:
                count+=1
        return count
