class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def delta(s1,s2):
            ans=[]
            for i in s1:
                if i not in s2:
                    ans.append(i)
            return ans
        s1=set(nums1)
        s2=set(nums2)
        return [
            delta(s1,s2),
            delta(s2,s1)
        ]