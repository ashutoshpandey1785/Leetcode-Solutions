class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if max(nums)<target:
            return len(nums)
        if target in nums:
            return nums.index(target)
        for i in nums:
            if i>target:
                return nums.index(i)
            # elif nums[i]==target:
            #     return i
            # elif nums[i]<target and nums[i+1]>target:
            #     return i+1
            