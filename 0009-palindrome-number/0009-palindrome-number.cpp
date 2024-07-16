class Solution {
public:
    bool isPalindrome(int x) {
        long long dup=x;
        long long rev=0;
        if (x < 0) {
            return false;
        }
        while(x){
            int ld=x%10;
            x=x/10;
            rev=(rev*10)+ld;
        }
        return rev==dup;
    }
};