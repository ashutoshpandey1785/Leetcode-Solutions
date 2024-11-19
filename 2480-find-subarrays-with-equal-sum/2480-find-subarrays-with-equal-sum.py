class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_set = set()

        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] in sum_set:
                return True
            sum_set.add(nums[i] + nums[i + 1])
        
        return False

        