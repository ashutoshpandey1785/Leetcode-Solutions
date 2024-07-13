class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=0
        m=sum(prices)
        for i in prices:
            m=min(m,i)
            r=max(r,i-m)
        return r