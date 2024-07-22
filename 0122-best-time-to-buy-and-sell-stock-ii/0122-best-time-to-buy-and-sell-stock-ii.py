class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        s=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if prices[i]>=s:
                s=prices[i]
            else:
                ans+=s-b
                b=prices[i]
                s=prices[i]
        ans+=s-b
        return ans