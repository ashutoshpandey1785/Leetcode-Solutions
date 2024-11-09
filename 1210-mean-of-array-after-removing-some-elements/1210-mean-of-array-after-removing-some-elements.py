class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=len(arr)
        p=int(0.05 * n)
        arr.sort()
        a=arr[p:n-p]
        b=sum(a)/len(a)
        return b
