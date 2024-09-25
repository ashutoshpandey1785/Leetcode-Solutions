class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        res = []

        for char in date.split('-'):
            b = bin(int(char))
            res.append(b[2:])
        
        return '-'.join(res)