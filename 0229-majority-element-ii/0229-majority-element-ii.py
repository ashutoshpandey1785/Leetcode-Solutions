class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m=len(nums)//3
        l=[]
        for i in nums:
            if nums.count(i)>m:
                if i not in l: # it will avoid duplicate terms
                    l.append(i)
        return l