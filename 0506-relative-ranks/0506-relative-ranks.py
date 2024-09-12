class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order=sorted(score,reverse=True)
        ans=[]
        for i in score:
            pos=order.index(i)
            if pos==0:
                ans.append("Gold Medal")
            elif pos==1:
                ans.append("Silver Medal")
            elif pos==2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(pos+1))
        return ans