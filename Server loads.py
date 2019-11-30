class Solution {
public:
    int findMinDiff(vector<int> servers) {
        int sum = accumulate(servers.begin(), servers.end(),0);
        
        //0 means sum can't be created by using specified numbers
        vector<vector<int>> dp(servers.size()+1, vector<int>(sum+1, 0));
        
        //Fill base cases
        for (int j = 1; j < sum+1; j++) dp[0][j] = 0; // Can't creat sum>0 with 0 numbers
        for (int i = 0; i < servers.size()+1; i++) dp[i][0] = 1; // Can create sum 0 with any numbers
        
        for (int i = 1; i < servers.size()+1; i++) {
            for (int j = 1; j < sum+1; j++) {
                //Not including server at index i-1
                dp[i][j] = dp[i-1][j];
                
                //Including it
                if (j>=servers[i-1]) {
                    dp[i][j] |= dp[i-1][j-servers[i-1]];    
                }
            }
        }
        
        //We want a value close to sum/2 to minimize difference
        int res = 0;
        for (int j = sum/2; j>=0; j--) {
            if (dp[servers.size()][j] == 1) {
                res = (sum-j)-j;  
                break;
            }
        }
        return res;
    }
};
int main() {
    Solution s = Solution();
    vector<int> servers = {1, 2, 3, 4, 5};
    cout << s.findMinDiff(servers);
}