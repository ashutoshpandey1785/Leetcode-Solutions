class Solution {
public:
    int countTestedDevices(vector<int>& batteryPercentages) {
        int ans=0;
        for(int i=0;i<batteryPercentages.size();i++){
            if(batteryPercentages[i]-ans<=0){
                continue;
            }
            else{
                ans+=1;
            }

        }
        return ans;
    }
};