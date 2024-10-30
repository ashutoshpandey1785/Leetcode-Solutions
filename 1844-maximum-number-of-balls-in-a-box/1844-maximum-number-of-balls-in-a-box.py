class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d=dict()
        for i in range(lowLimit,highLimit+1):
            s=str(i)
            c=0
            for i in s:
                c+=int(i)
            if(c in d):
                d[c]+=1
            else:
                d[c]=1
        return max(d.values())
