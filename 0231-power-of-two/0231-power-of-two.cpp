#include<cmath>
class Solution {
public:
    bool isPowerOfTwo(int n) {
        // int ans=1,i;
        for (int i=0;i<=30;i++){
            int ans=pow(2,i);
            if(ans==n){
                return true;
            } 
        }
        return false;
    }
};