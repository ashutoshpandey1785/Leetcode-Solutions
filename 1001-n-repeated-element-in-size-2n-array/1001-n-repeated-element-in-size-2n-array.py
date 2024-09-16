class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l1=[]
        for i in nums:
            if i in l1:
                return i
            else:
                l1.append(i)