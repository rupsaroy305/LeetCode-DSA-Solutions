class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1||numRows>=s.size())
            return s;
        vector<string>rows(numRows);
        int row=0;
        bool down=true;
        for(int i=0;i<s.size();i++){
            rows[row]+=s[i];
            if(row==0)
                down=true;
            else if(row==numRows-1)
                down=false;
            if(down)
                row++;
            else
                row--;
        }
        string ans="";
        for(int i=0;i<numRows;i++)
            ans+=rows[i];
        return ans;
    }
};