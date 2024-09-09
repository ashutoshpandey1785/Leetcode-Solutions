class Solution(object):
    def searchRange(self, nums, target):
        for i in range(len(nums)):
            if(nums[i]==target):
                a=i
                break
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]==target):
                b=i
                break
        if target not in nums:
            return [-1,-1]
        return [a,b]