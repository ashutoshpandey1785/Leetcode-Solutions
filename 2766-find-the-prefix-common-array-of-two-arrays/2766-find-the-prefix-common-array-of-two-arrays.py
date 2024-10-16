class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1=set()
        s2=set()
        res=[]
        for i in range(len(B)):
            s1.add(A[i])
            s2.add(B[i])
            res.append(len(s1.intersection(s2)))
        return res