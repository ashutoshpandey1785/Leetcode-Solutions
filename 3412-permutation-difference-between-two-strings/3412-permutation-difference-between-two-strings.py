class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans=0
        for i in s:
            ans+=abs(s.index(i)-t.index(i))
        return ans