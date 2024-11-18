class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums=set()
        half=sum(nums)/2
        if not half.is_integer():
            return False
        for i in nums:
            for j in sums.copy():
                if j+i<=half:
                    sums.add(j+i)
            sums.add(i)
            if half in sums:
                return True
        return False     