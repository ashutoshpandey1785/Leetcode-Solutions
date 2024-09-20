class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        j=0
        for i in range(len(s)):
            if g[j]<=s[i]:
                j+=1
                ans+=1
            if j==len(g):
                break
        return ans