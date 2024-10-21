class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a=[]
        cnt = Counter(arr)
        for i, j in cnt.items():
            if j == 1:
                a.append(i)

        if len(a) < k:
            return ""
        else:
            return a[k-1]