class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n=nums.size();
        vector<long long> prefix(n+1,0);
        for(int i=0;i<n;i++)
            prefix[i+1]=prefix[i]+nums[i];
        int ans=n+1;
        for(int i=0;i<n;i++){
            long long need=prefix[i]+target;
            int pos=lower_bound(prefix.begin(),prefix.end(),need)-prefix.begin();
            if(pos<=n)
                ans=min(ans,pos-i);
        }
        if(ans==n+1)
            return 0;
        return ans;
    }
};
