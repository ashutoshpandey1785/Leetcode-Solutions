class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=sum(nums)
        b=sum(set(nums))
        s=len(nums)*(len(nums)+1)//2
        return [a-b,s-b]