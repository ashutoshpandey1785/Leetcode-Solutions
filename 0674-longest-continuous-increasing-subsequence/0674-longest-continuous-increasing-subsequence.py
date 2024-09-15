class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count =1
        max_count=0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                count=1
            if count>max_count:
                max_count=count
        return max_count