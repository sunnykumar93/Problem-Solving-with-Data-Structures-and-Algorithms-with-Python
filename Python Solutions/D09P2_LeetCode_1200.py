class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_dif=float("inf")
        l=[]
        arr.sort()
        for i in range(len(arr)-1):
            if min_dif>abs(arr[i]-arr[i+1]):
                min_dif=abs(arr[i]-arr[i+1])
        
        for i in range(len(arr)-1):
            if (abs(arr[i]-arr[i+1])==min_dif):
                l.append([arr[i],arr[i+1]])
        return l
        
