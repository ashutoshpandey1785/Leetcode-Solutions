class Solution:
    def romanToInt(self, s: str) -> int:
        check={'I'   :  1,
        'V'  :          5,
        'X'   :        10,
        'L'    :       50,
        'C'   :      100,
        'D'      :     500,
        'M'     :    1000}
        r=0
        for i in range(len(s)):
            if i+1 < len(s) and check[s[i]]< check[s[i+1]] :
                r -= check[s[i]]
            else:
                r+=check[s[i]]
        return r
