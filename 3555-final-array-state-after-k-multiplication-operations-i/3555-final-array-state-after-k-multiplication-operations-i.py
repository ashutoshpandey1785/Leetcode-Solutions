class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_indx=nums.index(min(nums))
            nums[min_indx]*=multiplier
        return nums
        
        