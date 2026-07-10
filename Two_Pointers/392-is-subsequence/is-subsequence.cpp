class Solution {
public:
    bool isSubsequence(string s, string t) {
        int pos=0;
        for(int i=0;i<s.size();i++){
            bool found=false;
            for(int j=pos;j<t.size();j++){
                if(s[i]==t[j]){
                    pos=j+1;
                    found=true;
                    break;
                }
            }
            if(!found)
                return false;
        }
        return true;
    }
};