class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        co=0
        for i in nums:
            ans=nums.count(i)
            if ans==1:
                co+=i
        return co