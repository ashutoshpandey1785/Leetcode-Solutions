class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        ma=max(nums)
        mi=min(nums)
        ans=((ma-k)-(mi+k))
        if ans>0:
            return ans
        else:
            return 0