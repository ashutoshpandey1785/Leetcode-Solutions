class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        final=[]
        for i in nums:
            if i%2==0:
                final.append(i)
            else:
                continue
        for j in nums:
            if j%2!=0:
                final.append(j)
        return final