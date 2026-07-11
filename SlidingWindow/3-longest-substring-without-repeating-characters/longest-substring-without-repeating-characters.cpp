class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans=0;
        for(int i=0;i<s.size();i++){
            vector<int> seen(256,0);
            int len=0;
            for(int j=i;j<s.size();j++){
                if(seen[s[j]])
                    break;
                seen[s[j]]=1;
                len++;
            }
            ans=max(ans,len);
        }
        return ans;
    }
};