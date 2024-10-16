class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen=set()
        result=0
        for i in nums:
            if i in seen:
                result^=i
            else:
                seen.add(i)
        return result