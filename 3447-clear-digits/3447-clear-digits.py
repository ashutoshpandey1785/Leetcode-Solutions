class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        m="0123456789"
        for i in s:
            if i in m and m:
                l.pop()
            else:
                l.append(i)
        return ''.join(l)