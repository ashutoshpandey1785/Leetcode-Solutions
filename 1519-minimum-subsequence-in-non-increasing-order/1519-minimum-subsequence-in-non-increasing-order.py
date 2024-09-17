class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        s = sum(nums)
        for i in range(len(nums)-1,-1,-1):
            ans.append(nums[i])
            if sum(ans)> s-sum(ans):
                return ans


        