class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        a=[]
        res=[]
        for i in range(1,m+1):
            a.append(i)
        for i in queries:
            res.append(a.index(i))
            a.remove(i)
            a.insert(0,i)
        return res