class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=1
        occurance=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                occurance+=1
            else:
                occurance=1
            
            if occurance<=2:
                nums[res]=nums[i]  #if occurance is more than 2 then inc res pointer
                res+=1
        return res                