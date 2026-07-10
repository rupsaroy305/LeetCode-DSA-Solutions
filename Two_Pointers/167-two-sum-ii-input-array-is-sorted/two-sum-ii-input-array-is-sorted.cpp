class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i=0;i<numbers.size();i++){
            int left=i+1;
            int right=numbers.size()-1;
            while(left<=right){
                int mid=(left+right)/2;
                if(numbers[mid]==target-numbers[i])
                    return {i+1,mid+1};
                if(numbers[mid]<target-numbers[i])
                    left=mid+1;
                else
                    right=mid-1;
            }
        }
        return {};
    }
};