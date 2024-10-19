class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            ans.append(int(str(i)[::-1]))
        nums+=ans
        return len(set(nums))
