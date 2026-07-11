class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        for(int i=0;i<nums.size();i++){
            if(i>0 && nums[i]==nums[i-1])
                continue;
            for(int j=i+1;j<nums.size();j++){
                if(j>i+1 && nums[j]==nums[j-1])
                    continue;
                int target=-(nums[i]+nums[j]);
                int left=j+1;
                int right=nums.size()-1;
                while(left<=right){
                    int mid=(left+right)/2;
                    if(nums[mid]==target){
                        ans.push_back({nums[i],nums[j],nums[mid]});
                        break;
                    }
                    if(nums[mid]<target)
                        left=mid+1;
                    else
                        right=mid-1;
                }
            }
        }
        return ans;
    }
};