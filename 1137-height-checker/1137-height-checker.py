class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_hight=sorted(heights)
        c=0
        for i in range(len(sort_hight)):
            if sort_hight[i]!=heights[i]:
                c+=1
        return c
