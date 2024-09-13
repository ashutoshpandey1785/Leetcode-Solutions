from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c=Counter(nums)
        max_len=0
        for i in c:
            if i+1 in c:
                max_len = max(max_len, c[i] + c[i + 1])
        return max_len