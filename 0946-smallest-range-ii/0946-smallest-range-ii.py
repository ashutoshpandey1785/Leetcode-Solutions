class Solution:
    def smallestRangeII(self, n: List[int], k: int) -> int:
        n.sort(reverse=1)
        r,l=n[0],n[~0]
        if (d:=r-l)<k:return d
        k+=k
        z=l+k
        while n:
            a=n.pop()+k
            q=z
            if n:
                a=max(a,n[0])
                q=min(q,n[-1])
            d=min(d,a-q)
        return d       