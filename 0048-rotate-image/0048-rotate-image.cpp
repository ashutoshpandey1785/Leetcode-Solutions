class Solution {
private:
    void reversemat(vector<int>& row){
        int l=0;
        int r=row.size()-1;
        while(l<r){
            swap(row[l],row[r]);
            l++;
            r--;
            
        }
    }
public:
    void rotate(vector<vector<int>>& matrix) {
       int row=matrix.size();
       for(int i=0;i<row;i++){
        for (int j=0;j<i;j++){
            swap(matrix[i][j],matrix[j][i]);

        }
       }
       for(int k=0;k<row;k++){
        reversemat(matrix[k]);
       }
    }
};