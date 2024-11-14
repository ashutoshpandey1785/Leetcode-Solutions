class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        sett=len(set(candyType))
        return min(n,sett)