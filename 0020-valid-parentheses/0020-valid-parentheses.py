class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in '([{':
                st.append(i)
            elif i in ')]}' and  not st:
                return False
            elif i==')' and st[-1]!='(':
                return False
            elif i==']' and st[-1]!='[':
                return False
            elif i=='}' and st[-1]!='{':
                return False
            else:
                st.pop()
        if not st:
            return True
        return False
                