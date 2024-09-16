class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ma=max(nums)
        ind=nums.index(ma)
        for i in range(len(nums)):
            if (nums[i])==ma:
                continue
            elif ma-(nums[i]*2)<0:
                return -1
        return ind