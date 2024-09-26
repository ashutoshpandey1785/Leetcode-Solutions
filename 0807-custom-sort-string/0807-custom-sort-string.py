class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=""
        for i in order:
            if i in s:
                c=s.count(i)
                ans+=c*i
        for i in s:
            if i not in ans:
                c=s.count(i)
                ans+=c*i
        return ans