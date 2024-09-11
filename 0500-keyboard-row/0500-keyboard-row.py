class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        fr=set("qwertyuiopQWERTYUIOP")
        sr=set("asdfghjklASDFGHJKL")
        tr=set("zxcvbnmZXCVBNM")
        for i in words:
            st=set(i)
            if st.issubset(fr) or st.issubset(sr) or st.issubset(tr):
                ans.append(i)
        return ans