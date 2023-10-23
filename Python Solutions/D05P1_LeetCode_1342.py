class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        if num==0:
            return count
        while num>0:
            if num%2==0:
                count+=1
            else:
                count+=2
            num=num>>1

            
            
        return count-1
