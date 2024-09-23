class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        if(matrix.empty()) return ans;  // Handle empty matrix

        int row = matrix.size();
        int col = matrix[0].size();  // Get the correct column size
        int count = 0;
        int total = row * col;
        
        // Index initialization
        int startingRow = 0;
        int startingCol = 0;
        int endingRow = row - 1;
        int endingCol = col - 1;

        while(count < total){
            // Print starting row
            for(int index = startingCol; count < total && index <= endingCol; index++){
                ans.push_back(matrix[startingRow][index]);
                count++;
            }
            startingRow++;        

            // Print ending column
            for(int index = startingRow; count < total && index <= endingRow; index++){
                ans.push_back(matrix[index][endingCol]);
                count++;
            }
            endingCol--;

            // Print ending row
            for(int index = endingCol; count < total && index >= startingCol; index--){
                ans.push_back(matrix[endingRow][index]);
                count++;
            }
            endingRow--;  

            // Print starting column
            for(int index = endingRow; count < total && index >= startingRow; index--){
                ans.push_back(matrix[index][startingCol]);
                count++;
            }
            startingCol++;    
        }
        return ans;
    }
};
