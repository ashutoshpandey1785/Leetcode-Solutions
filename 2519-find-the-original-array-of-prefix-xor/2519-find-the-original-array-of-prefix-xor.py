class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[]
        ans.append(pref[0])
        for i in range(0,len(pref)-1):
            ans.append(pref[i]^pref[i+1])
        return ans
        