class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if ans<sum:
                ans=sum
            if sum<0:
                sum=0
        return ans